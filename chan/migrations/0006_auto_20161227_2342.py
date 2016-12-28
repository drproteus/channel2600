# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chan', '0005_auto_20161227_2244'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(default=b'Anonymous', max_length=80),
        ),
        migrations.AddField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 27, 23, 42, 31, 410170, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reply',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 27, 23, 42, 38, 466373, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='thread',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 27, 23, 42, 42, 258468, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
