# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chan', '0009_auto_20161228_0335'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='filename',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='filesize',
            field=models.DecimalField(default=0, max_digits=100, decimal_places=1),
        ),
        migrations.AddField(
            model_name='post',
            name='height',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='width',
            field=models.IntegerField(default=0, blank=True),
        ),
    ]
