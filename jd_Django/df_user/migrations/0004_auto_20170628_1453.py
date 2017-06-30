# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('df_user', '0003_useraddress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddress',
            name='default_addr',
            field=models.BooleanField(default=False),
        ),
    ]
