# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='python41_user',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_name', models.CharField(max_length=32)),
                ('user_email', models.CharField(default=b'', max_length=64)),
                ('user_pwd', models.CharField(max_length=40)),
                ('openid', models.CharField(default=b'', max_length=32)),
                ('user_sex', models.BooleanField(default=False)),
                ('user_weight', models.DecimalField(default=0, max_digits=5, decimal_places=2)),
                ('user_height', models.DecimalField(default=0, max_digits=5, decimal_places=2)),
                ('user_logo', models.ImageField(upload_to=b'user_logo')),
                ('user_tel', models.CharField(default=b'', max_length=20)),
                ('user_identify', models.CharField(default=b'', max_length=20)),
                ('user_check', models.CharField(default=b'0', max_length=10)),
                ('user_check_code', models.CharField(default=b'', max_length=32)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
    ]
