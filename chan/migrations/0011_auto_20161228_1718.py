# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chan', '0010_auto_20161228_1632'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='locked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='thread',
            name='sticky',
            field=models.BooleanField(default=False),
        ),
    ]
