# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20151028_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stats',
            name='activity',
            field=models.ForeignKey(to='api.Activity'),
        ),
    ]
