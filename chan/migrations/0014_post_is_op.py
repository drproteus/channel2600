# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chan', '0013_auto_20161230_0158'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_op',
            field=models.BooleanField(default=False),
        ),
    ]
