# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kindergarten',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=300)),
                ('address', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=400)),
                ('city_code', models.IntegerField(default=21)),
                ('email', models.EmailField(max_length=254)),
                ('capacity', models.IntegerField(default=0)),
            ],
        ),
    ]
