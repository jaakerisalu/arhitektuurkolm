# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
# Jaak: NEVERMIND THE DATABASE IS ABYSMAL, I WILL FIX IT.
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from accounts.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Address(models.Model):
    """
        An Enterprise or a Person can have an address
    """
    PERSONAL_ADDRESS = 1
    SECONDARY_ADDRESS = 2
    BUSINESS_ADDRESS = 3
    TYPE_CHOICES = (
        (PERSONAL_ADDRESS, 'Personal primary address'),
        (SECONDARY_ADDRESS, 'Secondary address'),
        (BUSINESS_ADDRESS, 'Business address'),
    )

    country = models.CharField(max_length=50, blank=True, null=True)
    county = models.CharField(max_length=100, blank=True, null=True)
    town_village = models.CharField(max_length=100, blank=True, null=True)
    street_address = models.CharField(max_length=100, blank=True, null=True)
    zipcode = models.CharField(max_length=50, blank=True, null=True)

    type = models.PositiveSmallIntegerField(choices=TYPE_CHOICES, blank=True, null=True)

    class Meta:
        verbose_name_plural = "addresses"

    def __str__(self):
        values = [str(self.country), str(self.county), str(self.town_village), str(self.street_address), str(self.zipcode)]
        return "Address: " + "/".join(values)


class Enterprise(models.Model):
    name = models.TextField(blank=True, null=True)
    full_name = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey("Employee", related_name="ent_created_by", blank=True, null=True)
    updated_by = models.ForeignKey("Employee", related_name="ent_updated_by", blank=True, null=True)
    created = models.DateTimeField(default=datetime.now, blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)

    is_customer = models.BooleanField(default=False)

    # They might have an address
    address = models.ForeignKey(Address, null=True, blank=True)

    def __str__(self):
        return ("Customer: " if self.is_customer else "Enterprise: ") + str(self.full_name if self.full_name else self.name)


class EmployeeRole(models.Model):
    role_name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return "EmployeeRole: " + str(self.role_name)


class Employee(models.Model):
    enterprise = models.ForeignKey(Enterprise, blank=True, null=True)
    roles = models.ManyToManyField(EmployeeRole)
    user = models.OneToOneField(User)

    def __str__(self):
        values = [str(self.user.first_name + " " + self.user.last_name if self.user.first_name and self.user.last_name else "UNNAMED EMPLOYEE"), str(self.enterprise.name)]
        return "Employee: " + ", ".join(values)


class Person(models.Model):
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    identity_code = models.CharField(max_length=20, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)

    created_by = models.ForeignKey(Employee, blank=True, null=True, related_name="created_persons")
    updated_by = models.ForeignKey(Employee, blank=True, null=True, related_name="updated_persons")

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # There might not be a user attached
    user = models.OneToOneField(User, blank=True, null=True, related_name="persons")

    # There might be an enterprise
    enterprise = models.ForeignKey(Enterprise, blank=True, null=True, related_name="persons")

    # If the User is not an employee, they might be a lawyer or something
    relation_type = models.CharField(max_length=200, blank=True, null=True)

    # Might be used for a customer aswell
    is_customer = models.BooleanField(default=False)

    # They might have an address
    address = models.ForeignKey(Address, null=True, blank=True)

    def __str__(self):
        values = [str(self.first_name), str(self.last_name)]
        return "Person" + (" (Customer)" if self.is_customer else "") + ": " + "/".join(values)


class Contact(models.Model):
    limit = models.Q(app_label='arhitektuurkolm', model='Person') | models.Q(app_label='arhitektuurkolm', model='Enterprise')
    subject_fk = models.PositiveIntegerField(blank=True, null=True)
    contact_type_fk = models.ForeignKey(ContentType, limit_choices_to=limit)
    subject = GenericForeignKey('contact_type_fk', 'subject_fk')

    value_text = models.TextField(blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    order_by = models.PositiveIntegerField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['order_by']

    def __str__(self):
        values = [str(self.value_text), str(self.email if self.email else self.phone)]
        return "Contact: " + ", ".join(values)


class SubjectAttribute(models.Model):
    PERSON = 1
    ENTERPRISE = 2
    EMPLOYEE = 3
    CUSTOMER = 4
    BELONGS_TO_CHOICES = (
        (PERSON, 'Person'),
        (ENTERPRISE, 'Enterprise'),
        (EMPLOYEE, 'Employee'),
        (CUSTOMER, 'Customer'),
    )

    TEXT = 1
    NUMBER = 2
    DATE = 3
    DATA_TYPE_CHOICES = (
        (TEXT, 'Text'),
        (NUMBER, 'Number'),
        (DATE, 'Date'),
    )

    name = models.CharField(max_length=200, blank=True, null=True)

    data_type = models.PositiveSmallIntegerField(choices=DATA_TYPE_CHOICES)
    belongs_to_type = models.PositiveSmallIntegerField(choices=BELONGS_TO_CHOICES)

    is_required = models.BooleanField(default=True)

    order = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return "SubjectAttribute: " + str(self.name if self.name else "UNNAMED")


class SubjectAttributeValue(models.Model):
    def _get_possible_owners_q_object(self):
        """
            Limit the generic foreign key possibilities by type
        """
        q_map = {
            SubjectAttribute.PERSON: models.Q(app_label='arhitektuurkolm', model='Person'),
            SubjectAttribute.ENTERPRISE: models.Q(app_label='arhitektuurkolm', model='Enterprise'),
            SubjectAttribute.EMPLOYEE: models.Q(app_label='arhitektuurkolm', model='Employee'),
            SubjectAttribute.CUSTOMER: models.Q(app_label='arhitektuurkolm', model='Customer'),
        }

        return q_map[self.attribute_type.belongs_to_type]

    attribute_type = models.ForeignKey(SubjectAttribute, related_name="values")

    owner_fk = models.PositiveIntegerField(blank=True, null=True)
    owner_type = models.ForeignKey(ContentType, limit_choices_to=_get_possible_owners_q_object)
    belongs_to = GenericForeignKey('owner_type', 'owner_fk')

    value_text = models.TextField(blank=True, null=True)
    value_number = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    value_date = models.DateField(blank=True, null=True)

