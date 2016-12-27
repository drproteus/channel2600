# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chan', '0002_auto_20161227_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='parent_post',
            field=models.ForeignKey(related_name='replies', to='chan.Post'),
        ),
        migrations.AlterField(
            model_name='reply',
            name='post',
            field=models.ForeignKey(related_name='post_reply', to='chan.Post'),
        ),
    ]
