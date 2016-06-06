# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arhitektuurkolm', '0002_auto_20160606_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjectattribute',
            name='data_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Text'), (2, 'Number'), (3, 'Date')]),
        ),
    ]
