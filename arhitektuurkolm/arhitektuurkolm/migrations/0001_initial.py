# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountsUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(null=True, blank=True)),
                ('is_superuser', models.BooleanField()),
                ('email', models.CharField(unique=True, max_length=254)),
                ('name', models.CharField(max_length=255)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'managed': False,
                'db_table': 'accounts_user',
            },
        ),
        migrations.CreateModel(
            name='AccountsUserGroups',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
            ],
            options={
                'managed': False,
                'db_table': 'accounts_user_groups',
            },
        ),
        migrations.CreateModel(
            name='AccountsUserUserPermissions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
            ],
            options={
                'managed': False,
                'db_table': 'accounts_user_user_permissions',
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('address', models.DecimalField(decimal_places=0, max_digits=10, primary_key=True, serialize=False)),
                ('address_type_fk', models.DecimalField(decimal_places=0, null=True, blank=True, max_digits=10)),
                ('subject_fk', models.DecimalField(decimal_places=0, null=True, blank=True, max_digits=10)),
                ('subject_type_fk', models.DecimalField(decimal_places=0, null=True, blank=True, max_digits=10)),
                ('country', models.CharField(null=True, blank=True, max_length=50)),
                ('county', models.CharField(null=True, blank=True, max_length=100)),
                ('town_village', models.CharField(null=True, blank=True, max_length=100)),
                ('street_address', models.CharField(null=True, blank=True, max_length=100)),
                ('zipcode', models.CharField(null=True, blank=True, max_length=50)),
            ],
            options={
                'managed': False,
                'db_table': 'address',
            },
        ),
        migrations.CreateModel(
            name='AddressType',
            fields=[
                ('address_type', models.DecimalField(decimal_places=0, max_digits=10, primary_key=True, serialize=False)),
                ('type_name', models.CharField(null=True, blank=True, max_length=200)),
            ],
            options={
                'managed': False,
                'db_table': 'address_type',
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(unique=True, max_length=80)),
            ],
            options={
                'managed': False,
                'db_table': 'auth_group',
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
            ],
            options={
                'managed': False,
                'db_table': 'auth_group_permissions',
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'managed': False,
                'db_table': 'auth_permission',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('contact', models.DecimalField(decimal_places=0, max_digits=10, primary_key=True, serialize=False)),
                ('subject_fk', models.DecimalField(decimal_places=0, null=True, blank=True, max_digits=10)),
                ('contact_type_fk', models.DecimalField(decimal_places=0, null=True, blank=True, max_digits=10)),
                ('value_text', models.TextField(null=True, blank=True)),
                ('orderby', models.DecimalField(decimal_places=0, null=True, blank=True, max_digits=10)),
                ('subject_type_fk', models.DecimalField(decimal_places=0, null=True, blank=True, max_digits=10)),
                ('note', models.TextField(null=True, blank=True)),
            ],
            options={
                'managed': False,
                'db_table': 'contact',
            },
        ),
        migrations.CreateModel(
            name='ContactType',
            fields=[
                ('contact_type', models.DecimalField(decimal_places=0, max_digits=10, primary_key=True, serialize=False)),
                ('type_name', models.CharField(null=True, blank=True, max_length=200)),
            ],
            options={
                'managed': False,
                'db_table': 'contact_type',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer', models.DecimalField(decimal_places=0, max_digits=10, primary_key=True, serialize=False)),
                ('subject_fk', models.DecimalField(decimal_places=0, null=True, blank=True, max_digits=10)),
                ('subject_type_fk', models.DecimalField(decimal_places=0, null=True, blank=True, max_digits=10)),
            ],
            options={
                'managed': False,
                'db_table': 'customer',
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(null=True, blank=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'managed': False,
                'db_table': 'django_admin_log',
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'managed': False,
                'db_table': 'django_content_type',
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'managed': False,
                'db_table': 'django_migrations',
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'managed': False,
                'db_table': 'django_session',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee', models.DecimalField(decimal_places=0, max_digits=10, primary_key=True, serialize=False)),
                ('person_fk', models.DecimalField(decimal_places=0, null=True, blank=True, max_digits=10)),
                ('enterprise_fk', models.DecimalField(decimal_places=0, null=True, blank=True, max_digits=10)),
                ('struct_unit_fk', models.DecimalField(decimal_places=0, null=True, blank=True, max_digits=10)),
                ('active', models.CharField(null=True, blank=True, max_length=1)),
            ],
            options={
                'managed': False,
                'db_table': 'employee',
            },
        ),
        migrations.CreateModel(
            name='EmployeeRole',
            fields=[
                ('employee_role', models.DecimalField(decimal_places=0, max_digits=10, primary_key=True, serialize=False)),
                ('employee_fk', models.DecimalField(decimal_places=0, null=True, blank=True, max_digits=10)),
                ('employee_role_type_fk', models.DecimalField(decimal_places=0, null=True, blank=True, max_digits=10)),
                ('active', models.CharField(null=True, blank=True, max_length=1)),
            ],
            options={
                'managed': False,
                'db_table': 'employee_role',
            },
        ),
        migrations.CreateModel(
            name='EmployeeRoleType',
            fields=[
                ('employee_role_type', models.DecimalField(decimal_places=0, max_digits=10, primary_key=True, serialize=False)),
                ('type_name', models.CharField(null=True, blank=True, max_length=200)),
            ],
            options={
                'managed': False,
                'db_table': 'employee_role_type',
            },
        ),
        migrations.CreateModel(
            name='Enterprise',
            fields=[
                ('enterprise', models.DecimalField(decimal_places=0, max_digits=10, primary_key=True, serialize=False)),
                ('name', models.TextField(null=True, blank=True)),
                ('full_name', models.TextField(null=True, blank=True)),
                ('created_by', models.DecimalField(decimal_places=0, null=True, blank=True, max_digits=10)),
                ('updated_by', models.DecimalField(decimal_places=0, null=True, blank=True, max_digits=10)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'managed': False,
                'db_table': 'enterprise',
            },
        ),
        migrations.CreateModel(
            name='EnterprisePersonRelation',
            fields=[
                ('enterprise_person_relation', models.DecimalField(decimal_places=0, max_digits=10, primary_key=True, serialize=False)),
                ('person_fk', models.DecimalField(decimal_places=0, null=True, blank=True, max_digits=10)),
                ('enterprise_fk', models.DecimalField(decimal_places=0, null=True, blank=True, max_digits=10)),
                ('ent_per_relation_type_fk', models.DecimalField(decimal_places=0, null=True, blank=True, max_digits=10)),
            ],
            options={
                'managed': False,
                'db_table': 'enterprise_person_relation',
            },
        ),
        migrations.CreateModel(
            name='EntPerRelationType',
            fields=[
                ('ent_per_relation_type', models.DecimalField(decimal_places=0, max_digits=10, primary_key=True, serialize=False)),
                ('type_name', models.CharField(null=True, blank=True, max_length=200)),
            ],
            options={
                'managed': False,
                'db_table': 'ent_per_relation_type',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('person', models.DecimalField(decimal_places=0, max_digits=10, primary_key=True, serialize=False)),
                ('first_name', models.CharField(null=True, blank=True, max_length=100)),
                ('last_name', models.CharField(null=True, blank=True, max_length=100)),
                ('identity_code', models.CharField(null=True, blank=True, max_length=20)),
                ('birth_date', models.DateField(null=True, blank=True)),
                ('created_by', models.DecimalField(decimal_places=0, null=True, blank=True, max_digits=10)),
                ('updated_by', models.DecimalField(decimal_places=0, null=True, blank=True, max_digits=10)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'managed': False,
                'db_table': 'person',
            },
        ),
        migrations.CreateModel(
            name='StructUnit',
            fields=[
                ('struct_unit', models.DecimalField(decimal_places=0, max_digits=10, primary_key=True, serialize=False)),
                ('enterprise_fk', models.DecimalField(decimal_places=0, null=True, blank=True, max_digits=10)),
                ('upper_unit_fk', models.DecimalField(decimal_places=0, null=True, blank=True, max_digits=10)),
                ('level', models.DecimalField(decimal_places=0, null=True, blank=True, max_digits=10)),
                ('name', models.CharField(null=True, blank=True, max_length=200)),
            ],
            options={
                'managed': False,
                'db_table': 'struct_unit',
            },
        ),
        migrations.CreateModel(
            name='SubjectAttribute',
            fields=[
                ('subject_attribute', models.DecimalField(decimal_places=0, max_digits=10, primary_key=True, serialize=False)),
                ('subject_fk', models.DecimalField(decimal_places=0, null=True, blank=True, max_digits=10)),
                ('subject_attribute_type_fk', models.DecimalField(decimal_places=0, null=True, blank=True, max_digits=10)),
                ('subject_type_fk', models.DecimalField(decimal_places=0, null=True, blank=True, max_digits=10)),
                ('orderby', models.DecimalField(decimal_places=0, null=True, blank=True, max_digits=10)),
                ('value_text', models.TextField(null=True, blank=True)),
                ('value_number', models.DecimalField(decimal_places=65535, null=True, blank=True, max_digits=65535)),
                ('value_date', models.DateField(null=True, blank=True)),
                ('data_type', models.DecimalField(decimal_places=0, null=True, blank=True, max_digits=1)),
            ],
            options={
                'managed': False,
                'db_table': 'subject_attribute',
            },
        ),
        migrations.CreateModel(
            name='SubjectAttributeType',
            fields=[
                ('subject_attribute_type', models.DecimalField(decimal_places=0, max_digits=10, primary_key=True, serialize=False)),
                ('subject_type_fk', models.DecimalField(decimal_places=0, null=True, blank=True, max_digits=10)),
                ('type_name', models.CharField(null=True, blank=True, max_length=200)),
                ('data_type', models.DecimalField(decimal_places=0, null=True, blank=True, max_digits=1)),
                ('orderby', models.DecimalField(decimal_places=0, null=True, blank=True, max_digits=10)),
                ('required', models.CharField(null=True, blank=True, max_length=1)),
                ('multiple_attributes', models.CharField(null=True, blank=True, max_length=1)),
                ('created_by_default', models.CharField(null=True, blank=True, max_length=1)),
            ],
            options={
                'managed': False,
                'db_table': 'subject_attribute_type',
            },
        ),
        migrations.CreateModel(
            name='SubjectType',
            fields=[
                ('subject_type', models.DecimalField(decimal_places=0, max_digits=10, primary_key=True, serialize=False)),
                ('type_name', models.CharField(null=True, blank=True, max_length=200)),
            ],
            options={
                'managed': False,
                'db_table': 'subject_type',
            },
        ),
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('user_account', models.DecimalField(decimal_places=0, max_digits=10, primary_key=True, serialize=False)),
                ('subject_type_fk', models.DecimalField(decimal_places=0, null=True, blank=True, max_digits=10)),
                ('subject_fk', models.DecimalField(decimal_places=0, null=True, blank=True, max_digits=10)),
                ('username', models.CharField(null=True, blank=True, max_length=50)),
                ('passw', models.CharField(null=True, blank=True, max_length=300)),
                ('status', models.DecimalField(decimal_places=0, null=True, blank=True, max_digits=10)),
                ('valid_from', models.DateField(null=True, blank=True)),
                ('valid_to', models.DateField(null=True, blank=True)),
                ('created_by', models.DecimalField(decimal_places=0, null=True, blank=True, max_digits=10)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('password_never_expires', models.CharField(null=True, blank=True, max_length=1)),
            ],
            options={
                'managed': False,
                'db_table': 'user_account',
            },
        ),
    ]
