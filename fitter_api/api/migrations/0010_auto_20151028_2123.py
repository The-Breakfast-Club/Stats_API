# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20151028_2013'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='stats',
            unique_together=set([('activity', 'date')]),
        ),
    ]
