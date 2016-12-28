# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chan', '0003_auto_20161227_2101'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='subject',
            field=models.CharField(default=b'', max_length=80),
        ),
    ]
