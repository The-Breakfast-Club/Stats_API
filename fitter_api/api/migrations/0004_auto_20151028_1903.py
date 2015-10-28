# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20151028_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='stats',
            name='activity',
            field=models.ForeignKey(to='api.Activity', unique_for_date='date'),
        ),
        migrations.AlterField(
            model_name='stats',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
