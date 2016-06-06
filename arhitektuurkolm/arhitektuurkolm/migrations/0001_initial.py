# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('subject_fk', models.PositiveIntegerField(null=True, blank=True)),
                ('country', models.CharField(max_length=50, null=True, blank=True)),
                ('county', models.CharField(max_length=100, null=True, blank=True)),
                ('town_village', models.CharField(max_length=100, null=True, blank=True)),
                ('street_address', models.CharField(max_length=100, null=True, blank=True)),
                ('zipcode', models.CharField(max_length=50, null=True, blank=True)),
            ],
            options={
                'db_table': 'address',
            },
        ),
        migrations.CreateModel(
            name='AddressType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('type_name', models.CharField(max_length=200, null=True, blank=True)),
            ],
            options={
                'db_table': 'address_type',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('subject_fk', models.PositiveIntegerField(null=True, blank=True)),
                ('value_text', models.TextField(null=True, blank=True)),
                ('orderby', models.DecimalField(decimal_places=0, null=True, max_digits=10, blank=True)),
                ('note', models.TextField(null=True, blank=True)),
                ('contact_type_fk', models.ForeignKey(to='contenttypes.ContentType')),
            ],
            options={
                'db_table': 'contact',
            },
        ),
        migrations.CreateModel(
            name='ContactType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('type_name', models.CharField(max_length=200, null=True, blank=True)),
            ],
            options={
                'db_table': 'contact_type',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('subject_fk', models.PositiveIntegerField(null=True, blank=True)),
                ('subject_type_fk', models.ForeignKey(to='contenttypes.ContentType')),
            ],
            options={
                'db_table': 'customer',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('active', models.NullBooleanField()),
            ],
            options={
                'db_table': 'employee',
            },
        ),
        migrations.CreateModel(
            name='EmployeeRole',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('active', models.NullBooleanField()),
                ('employee_fk', models.ForeignKey(to='arhitektuurkolm.Employee', blank=True, null=True)),
            ],
            options={
                'db_table': 'employee_role',
            },
        ),
        migrations.CreateModel(
            name='EmployeeRoleType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('type_name', models.CharField(max_length=200, null=True, blank=True)),
            ],
            options={
                'db_table': 'employee_role_type',
            },
        ),
        migrations.CreateModel(
            name='Enterprise',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.TextField(null=True, blank=True)),
                ('full_name', models.TextField(null=True, blank=True)),
                ('created', models.DateTimeField(null=True, default=datetime.datetime.now, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('created_by', models.ForeignKey(to='arhitektuurkolm.Employee', related_name='ent_created_by', blank=True, null=True)),
                ('updated_by', models.ForeignKey(to='arhitektuurkolm.Employee', related_name='ent_updated_by', blank=True, null=True)),
            ],
            options={
                'db_table': 'enterprise',
            },
        ),
        migrations.CreateModel(
            name='EnterprisePersonRelation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'enterprise_person_relation',
            },
        ),
        migrations.CreateModel(
            name='EntPerRelationType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('type_name', models.CharField(max_length=200, null=True, blank=True)),
            ],
            options={
                'db_table': 'ent_per_relation_type',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('first_name', models.CharField(max_length=100, null=True, blank=True)),
                ('last_name', models.CharField(max_length=100, null=True, blank=True)),
                ('identity_code', models.CharField(max_length=20, null=True, blank=True)),
                ('birth_date', models.DateField(null=True, blank=True)),
                ('created', models.DateTimeField(null=True, default=datetime.datetime.now, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('created_by', models.ForeignKey(to='arhitektuurkolm.Employee', related_name='pers_created_by', blank=True, null=True)),
                ('updated_by', models.ForeignKey(to='arhitektuurkolm.Employee', related_name='pers_updated_by', blank=True, null=True)),
            ],
            options={
                'db_table': 'person',
            },
        ),
        migrations.CreateModel(
            name='StructUnit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('upper_unit_fk', models.PositiveIntegerField(null=True, blank=True)),
                ('level', models.PositiveIntegerField(null=True, blank=True)),
                ('name', models.CharField(max_length=200, null=True, blank=True)),
                ('enterprise_fk', models.ForeignKey(to='arhitektuurkolm.Enterprise', blank=True, null=True)),
            ],
            options={
                'db_table': 'struct_unit',
            },
        ),
        migrations.CreateModel(
            name='SubjectAttribute',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('subject_fk', models.PositiveIntegerField(null=True, blank=True)),
                ('orderby', models.IntegerField(null=True, blank=True)),
                ('value_text', models.TextField(null=True, blank=True)),
                ('value_number', models.DecimalField(decimal_places=0, null=True, max_digits=10, blank=True)),
                ('value_date', models.DateField(null=True, blank=True)),
                ('data_type', models.DecimalField(decimal_places=0, null=True, max_digits=1, blank=True)),
            ],
            options={
                'db_table': 'subject_attribute',
            },
        ),
        migrations.CreateModel(
            name='SubjectAttributeType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('type_name', models.CharField(max_length=200, null=True, blank=True)),
                ('data_type', models.DecimalField(decimal_places=0, null=True, max_digits=1, blank=True)),
                ('orderby', models.DecimalField(decimal_places=0, null=True, max_digits=10, blank=True)),
                ('required', models.NullBooleanField()),
                ('multiple_attributes', models.NullBooleanField()),
                ('created_by_default', models.NullBooleanField(default=True)),
            ],
            options={
                'db_table': 'subject_attribute_type',
            },
        ),
        migrations.CreateModel(
            name='SubjectType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('type_name', models.CharField(max_length=200, null=True, blank=True)),
            ],
            options={
                'db_table': 'subject_type',
            },
        ),
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('status', models.DecimalField(decimal_places=0, null=True, max_digits=10, blank=True)),
                ('valid_from', models.DateField(null=True, blank=True)),
                ('valid_to', models.DateField(null=True, blank=True)),
                ('created', models.DateTimeField(null=True, default=datetime.datetime.now, blank=True)),
                ('password_never_expires', models.NullBooleanField()),
                ('created_by', models.ForeignKey(to='arhitektuurkolm.Employee', related_name='user_created_by', blank=True, null=True)),
                ('subject_fk', models.ForeignKey(to='arhitektuurkolm.Employee', related_name='user_emp', blank=True, null=True)),
                ('subject_type_fk', models.ForeignKey(to='arhitektuurkolm.SubjectType', blank=True, null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_account',
            },
        ),
        migrations.AddField(
            model_name='subjectattributetype',
            name='subject_type_fk',
            field=models.ForeignKey(to='arhitektuurkolm.SubjectType', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='subjectattribute',
            name='subject_attribute_type_fk',
            field=models.ForeignKey(to='arhitektuurkolm.SubjectAttributeType', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='subjectattribute',
            name='subject_type_fk',
            field=models.ForeignKey(to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='enterprisepersonrelation',
            name='ent_per_relation_type_fk',
            field=models.ForeignKey(to='arhitektuurkolm.EntPerRelationType', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='enterprisepersonrelation',
            name='enterprise_fk',
            field=models.ForeignKey(to='arhitektuurkolm.Enterprise', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='enterprisepersonrelation',
            name='person_fk',
            field=models.ForeignKey(to='arhitektuurkolm.Person', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employeerole',
            name='employee_role_type_fk',
            field=models.ForeignKey(to='arhitektuurkolm.EmployeeRoleType', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='enterprise_fk',
            field=models.ForeignKey(to='arhitektuurkolm.Enterprise', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='person_fk',
            field=models.ForeignKey(to='arhitektuurkolm.Person', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='struct_unit_fk',
            field=models.ForeignKey(to='arhitektuurkolm.StructUnit', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='subject_type_fk',
            field=models.ForeignKey(to='arhitektuurkolm.SubjectType', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='address_type_fk',
            field=models.ForeignKey(to='arhitektuurkolm.AddressType', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='subject_type_fk',
            field=models.ForeignKey(to='contenttypes.ContentType'),
        ),
    ]
