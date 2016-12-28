# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import cloudinary.models


class Migration(migrations.Migration):

    dependencies = [
        ('chan', '0006_auto_20161227_2342'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name=b'image', blank=True),
        ),
    ]
