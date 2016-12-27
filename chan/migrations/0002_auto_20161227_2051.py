# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chan', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='parent_post',
            field=models.ForeignKey(related_name='post_parent_post', default=0, to='chan.Post'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reply',
            name='post',
            field=models.ForeignKey(related_name='post_reply_post', to='chan.Post'),
        ),
    ]
