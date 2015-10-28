# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20151028_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stats',
            name='date',
            field=models.DateField(),
        ),
    ]
