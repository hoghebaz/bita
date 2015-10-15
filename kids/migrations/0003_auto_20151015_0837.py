# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kids', '0002_remove_kindergarten_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='kindergarten',
            name='phone_number',
            field=models.CharField(default=b' ', max_length=12),
        ),
        migrations.AlterField(
            model_name='kindergarten',
            name='city_code',
            field=models.CharField(max_length=6),
        ),
    ]
