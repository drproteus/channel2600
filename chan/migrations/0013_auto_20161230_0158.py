# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chan', '0012_thread_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(default='Anonymous', max_length=80),
        ),
        migrations.AlterField(
            model_name='thread',
            name='subject',
            field=models.CharField(default='', max_length=80),
        ),
    ]
