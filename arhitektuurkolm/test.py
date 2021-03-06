# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Address(models.Model):
    address = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    address_type_fk = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    subject_fk = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    subject_type_fk = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    county = models.CharField(max_length=100, blank=True, null=True)
    town_village = models.CharField(max_length=100, blank=True, null=True)
    street_address = models.CharField(max_length=100, blank=True, null=True)
    zipcode = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'address'


class AddressType(models.Model):
    address_type = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    type_name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'address_type'


class Contact(models.Model):
    contact = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    subject_fk = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    contact_type_fk = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    value_text = models.TextField(blank=True, null=True)
    orderby = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    subject_type_fk = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    note = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contact'


class ContactType(models.Model):
    contact_type = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    type_name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contact_type'


class Customer(models.Model):
    customer = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    subject_fk = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    subject_type_fk = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer'


class Employee(models.Model):
    employee = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    person_fk = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    enterprise_fk = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    struct_unit_fk = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    active = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee'


class EmployeeRole(models.Model):
    employee_role = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    employee_fk = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    employee_role_type_fk = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    active = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee_role'


class EmployeeRoleType(models.Model):
    employee_role_type = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    type_name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee_role_type'


class EntPerRelationType(models.Model):
    ent_per_relation_type = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    type_name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ent_per_relation_type'


class Enterprise(models.Model):
    enterprise = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    name = models.TextField(blank=True, null=True)
    full_name = models.TextField(blank=True, null=True)
    created_by = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    updated_by = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enterprise'


class EnterprisePersonRelation(models.Model):
    enterprise_person_relation = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    person_fk = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    enterprise_fk = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    ent_per_relation_type_fk = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enterprise_person_relation'


class Person(models.Model):
    person = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    identity_code = models.CharField(max_length=20, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    created_by = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    updated_by = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'person'


class StructUnit(models.Model):
    struct_unit = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    enterprise_fk = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    upper_unit_fk = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    level = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'struct_unit'


class SubjectAttribute(models.Model):
    subject_attribute = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    subject_fk = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    subject_attribute_type_fk = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    subject_type_fk = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    orderby = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    value_text = models.TextField(blank=True, null=True)
    value_number = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    value_date = models.DateField(blank=True, null=True)
    data_type = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subject_attribute'


class SubjectAttributeType(models.Model):
    subject_attribute_type = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    subject_type_fk = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    type_name = models.CharField(max_length=200, blank=True, null=True)
    data_type = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    orderby = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    required = models.CharField(max_length=1, blank=True, null=True)
    multiple_attributes = models.CharField(max_length=1, blank=True, null=True)
    created_by_default = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subject_attribute_type'


class SubjectType(models.Model):
    subject_type = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    type_name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subject_type'


class UserAccount(models.Model):
    user_account = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    subject_type_fk = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    subject_fk = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    passw = models.CharField(max_length=300, blank=True, null=True)
    status = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    valid_from = models.DateField(blank=True, null=True)
    valid_to = models.DateField(blank=True, null=True)
    created_by = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    password_never_expires = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_account'
