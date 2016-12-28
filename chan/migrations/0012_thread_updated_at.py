# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chan', '0011_auto_20161228_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 28, 19, 38, 11, 151669, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
