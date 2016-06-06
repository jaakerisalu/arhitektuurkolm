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
from datetime import datetime
from accounts.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType



class Address(models.Model):
    address_type_fk = models.ForeignKey("AddressType", blank=True, null=True)
    limit = models.Q(app_label='arhitektuurkolm', model='Person') | models.Q(app_label='arhitektuurkolm', model='Enterprise')
    subject_fk = models.PositiveIntegerField(blank=True, null=True)
    subject_type_fk = models.ForeignKey(ContentType, limit_choices_to=limit)
    subject = GenericForeignKey('subject_type_fk', 'subject_fk')
    country = models.CharField(max_length=50, blank=True, null=True)
    county = models.CharField(max_length=100, blank=True, null=True)
    town_village = models.CharField(max_length=100, blank=True, null=True)
    street_address = models.CharField(max_length=100, blank=True, null=True)
    zipcode = models.CharField(max_length=50, blank=True, null=True)
    
    class Meta:
        db_table = 'address'

        
class AddressType(models.Model):
    type_name = models.CharField(max_length=200, blank=True, null=True)
    
    class Meta:
        db_table = 'address_type'


class Contact(models.Model):
    limit = models.Q(app_label='arhitektuurkolm', model='Person') | models.Q(app_label='arhitektuurkolm', model='Enterprise')
    subject_fk = models.PositiveIntegerField(blank=True, null=True)
    contact_type_fk = models.ForeignKey(ContentType, limit_choices_to=limit)
    subject = GenericForeignKey('contact_type_fk', 'subject_fk')
    value_text = models.TextField(blank=True, null=True)
    orderby = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    subject_type_fk = models.ForeignKey("SubjectType", blank=True, null=True)
    note = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'contact'


class ContactType(models.Model):
    type_name = models.CharField(max_length=200, blank=True, null=True)
    
    class Meta:
        db_table = 'contact_type'


class Customer(models.Model):

    limit = models.Q(app_label='arhitektuurkolm', model='Person') | models.Q(app_label='arhitektuurkolm', model='Enterprise')
    subject_fk = models.PositiveIntegerField(blank=True, null=True)
    subject_type_fk = models.ForeignKey(ContentType, limit_choices_to=limit)
    subject = GenericForeignKey('subject_type_fk', 'subject_fk')

    class Meta:
        db_table = 'customer'

        
class Employee(models.Model):
    person_fk = models.ForeignKey("Person", blank=True, null=True)
    enterprise_fk = models.ForeignKey("Enterprise", blank=True, null=True)
    struct_unit_fk = models.ForeignKey("StructUnit", blank=True, null=True)
    active = models.NullBooleanField(blank=True, null=True)
    
    class Meta:
        db_table = 'employee'
        

class EmployeeRole(models.Model):
    employee_fk = models.ForeignKey("Employee", blank=True, null=True)
    employee_role_type_fk = models.ForeignKey("EmployeeRoleType", blank=True, null=True)
    active = models.NullBooleanField(blank=True, null=True)
    
    class Meta:
        db_table = 'employee_role'


class EmployeeRoleType(models.Model):
    type_name = models.CharField(max_length=200, blank=True, null=True)
    
    class Meta:
        db_table = 'employee_role_type'


class EntPerRelationType(models.Model):
    type_name = models.CharField(max_length=200, blank=True, null=True)
    
    class Meta:
        db_table = 'ent_per_relation_type'


class Enterprise(models.Model):
    name = models.TextField(blank=True, null=True)
    full_name = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey("Employee", related_name="ent_created_by", blank=True, null=True)
    updated_by = models.ForeignKey("Employee", related_name="ent_updated_by", blank=True, null=True)
    created = models.DateTimeField(default=datetime.now, blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    
    class Meta:
       db_table = 'enterprise'

class EnterprisePersonRelation(models.Model):
    person_fk = models.ForeignKey("Person", blank=True, null=True)
    enterprise_fk = models.ForeignKey("Enterprise", blank=True, null=True)
    ent_per_relation_type_fk = models.ForeignKey("EntPerRelationType", blank=True, null=True)
    
    class Meta:
        db_table = 'enterprise_person_relation'

        
class Person(models.Model):
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    identity_code = models.CharField(max_length=20, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    created_by = models.ForeignKey("Employee", related_name="pers_created_by", blank=True, null=True)
    updated_by = models.ForeignKey("Employee", related_name="pers_updated_by", blank=True, null=True)
    created = models.DateTimeField(default=datetime.now, blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    
    class Meta:
        db_table = 'person'

class StructUnit(models.Model):
    enterprise_fk = models.ForeignKey("Enterprise", blank=True, null=True)
    upper_unit_fk = models.PositiveIntegerField(blank=True, null=True)
    level = models.PositiveIntegerField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    
    class Meta:
        db_table = 'struct_unit'

class SubjectAttribute(models.Model):

    limit = models.Q(app_label='arhitektuurkolm', model='Person') | models.Q(app_label='arhitektuurkolm', model='Enterprise') | models.Q(app_label='arhitektuurkolm', model='Employee') | models.Q(app_label='arhitektuurkolm', model='Customer')
    subject_fk = models.PositiveIntegerField(blank=True, null=True)
    subject_type_fk = models.ForeignKey(ContentType, limit_choices_to=limit)
    subject = GenericForeignKey('subject_type_fk', 'subject_fk')
    
    subject_attribute_type_fk = models.ForeignKey("SubjectAttributeType", blank=True, null=True)
    orderby = models.IntegerField(blank=True, null=True)
    value_text = models.TextField(blank=True, null=True)
    value_number = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    value_date = models.DateField(blank=True, null=True)
    data_type = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    
    class Meta:
        db_table = 'subject_attribute'

        
class SubjectAttributeType(models.Model):
    subject_type_fk = models.ForeignKey("SubjectType", blank=True, null=True)
    type_name = models.CharField(max_length=200, blank=True, null=True)
    data_type = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    orderby = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    required = models.NullBooleanField(blank=True, null=True)
    multiple_attributes = models.NullBooleanField(blank=True, null=True)
    created_by_default = models.NullBooleanField(default=True, blank=True, null=True)
    
    class Meta:
        db_table = 'subject_attribute_type'

        
class SubjectType(models.Model):
    type_name = models.CharField(max_length=200, blank=True, null=True)
    
    class Meta:
        db_table = 'subject_type'
        
        
class UserAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subject_type_fk = models.ForeignKey("SubjectType", blank=True, null=True) # alati 3
    subject_fk = models.ForeignKey("Employee", related_name="user_emp", blank=True, null=True)
    #username = models.CharField(max_length=50, blank=True, null=True)
    #passw = models.CharField(max_length=300, blank=True, null=True)
    status = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    valid_from = models.DateField(blank=True, null=True)
    valid_to = models.DateField(blank=True, null=True)
    created_by = models.ForeignKey("Employee", related_name="user_created_by", blank=True, null=True)
    created = models.DateTimeField(default=datetime.now, blank=True, null=True)
    password_never_expires = models.NullBooleanField(blank=True, null=True)
    
    class Meta:
        db_table = 'user_account'