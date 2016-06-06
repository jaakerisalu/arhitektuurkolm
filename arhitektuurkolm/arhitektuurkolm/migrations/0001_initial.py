# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('country', models.CharField(max_length=50, blank=True, null=True)),
                ('county', models.CharField(max_length=100, blank=True, null=True)),
                ('town_village', models.CharField(max_length=100, blank=True, null=True)),
                ('street_address', models.CharField(max_length=100, blank=True, null=True)),
                ('zipcode', models.CharField(max_length=50, blank=True, null=True)),
                ('type', models.PositiveSmallIntegerField(choices=[(1, 'Personal primary address'), (2, 'Secondary address'), (3, 'Business address')], blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('subject_fk', models.PositiveIntegerField(blank=True, null=True)),
                ('value_text', models.TextField(blank=True, null=True)),
                ('email', models.EmailField(max_length=100, blank=True, null=True)),
                ('phone', models.CharField(max_length=100, blank=True, null=True)),
                ('order_by', models.PositiveIntegerField(blank=True, null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('contact_type_fk', models.ForeignKey(to='contenttypes.ContentType')),
            ],
            options={
                'ordering': ['order_by'],
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeRole',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('role_name', models.CharField(max_length=200, blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Enterprise',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.TextField(blank=True, null=True)),
                ('full_name', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
                ('updated', models.DateTimeField(blank=True, null=True)),
                ('is_customer', models.BooleanField(default=False)),
                ('address', models.ForeignKey(blank=True, to='arhitektuurkolm.Address', null=True)),
                ('created_by', models.ForeignKey(related_name='ent_created_by', blank=True, to='arhitektuurkolm.Employee', null=True)),
                ('updated_by', models.ForeignKey(related_name='ent_updated_by', blank=True, to='arhitektuurkolm.Employee', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('first_name', models.CharField(max_length=100, blank=True, null=True)),
                ('last_name', models.CharField(max_length=100, blank=True, null=True)),
                ('identity_code', models.CharField(max_length=20, blank=True, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('relation_type', models.CharField(max_length=200, blank=True, null=True)),
                ('is_customer', models.BooleanField(default=False)),
                ('address', models.ForeignKey(blank=True, to='arhitektuurkolm.Address', null=True)),
                ('created_by', models.ForeignKey(related_name='created_persons', blank=True, to='arhitektuurkolm.Employee', null=True)),
                ('enterprise', models.ForeignKey(related_name='persons', blank=True, to='arhitektuurkolm.Enterprise', null=True)),
                ('updated_by', models.ForeignKey(related_name='updated_persons', blank=True, to='arhitektuurkolm.Employee', null=True)),
                ('user', models.OneToOneField(related_name='persons', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubjectAttribute',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200, blank=True, null=True)),
                ('value_text', models.TextField(blank=True, null=True)),
                ('value_number', models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=0)),
                ('value_date', models.DateField(blank=True, null=True)),
                ('data_type', models.PositiveSmallIntegerField(choices=[(1, 'Person'), (2, 'Enterprise'), (3, 'Employee'), (4, 'Customer')])),
                ('belongs_to', models.PositiveSmallIntegerField(choices=[(1, 'Person'), (2, 'Enterprise'), (3, 'Employee'), (4, 'Customer')])),
                ('is_required', models.BooleanField(default=True)),
                ('order', models.PositiveIntegerField(blank=True, null=True)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.AddField(
            model_name='employee',
            name='enterprise',
            field=models.ForeignKey(blank=True, to='arhitektuurkolm.Enterprise', null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='roles',
            field=models.ManyToManyField(to='arhitektuurkolm.EmployeeRole'),
        ),
        migrations.AddField(
            model_name='employee',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
