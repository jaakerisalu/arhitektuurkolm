# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('arhitektuurkolm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubjectAttributeValue',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('owner_fk', models.PositiveIntegerField(blank=True, null=True)),
                ('value_text', models.TextField(blank=True, null=True)),
                ('value_number', models.DecimalField(decimal_places=0, max_digits=10, blank=True, null=True)),
                ('value_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name_plural': 'addresses'},
        ),
        migrations.RenameField(
            model_name='subjectattribute',
            old_name='belongs_to',
            new_name='belongs_to_type',
        ),
        migrations.RemoveField(
            model_name='subjectattribute',
            name='value_date',
        ),
        migrations.RemoveField(
            model_name='subjectattribute',
            name='value_number',
        ),
        migrations.RemoveField(
            model_name='subjectattribute',
            name='value_text',
        ),
        migrations.AddField(
            model_name='subjectattributevalue',
            name='attribute_type',
            field=models.ForeignKey(related_name='values', to='arhitektuurkolm.SubjectAttribute'),
        ),
        migrations.AddField(
            model_name='subjectattributevalue',
            name='owner_type',
            field=models.ForeignKey(to='contenttypes.ContentType'),
        ),
    ]
