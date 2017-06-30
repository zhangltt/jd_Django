# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('df_user', '0002_python41_user_nick_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('consignee', models.CharField(default=b'', max_length=32)),
                ('address', models.CharField(default=b'', max_length=300)),
                ('iphone', models.CharField(default=b'', max_length=20)),
                ('default_addr', models.BooleanField(verbose_name=False)),
                ('uid', models.ForeignKey(to='df_user.python41_user')),
            ],
        ),
    ]
