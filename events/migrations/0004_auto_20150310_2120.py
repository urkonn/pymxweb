# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20150308_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_at',
            field=models.DateField(verbose_name='Termina a las'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='start_at',
            field=models.DateField(verbose_name='Comienza a las'),
            preserve_default=True,
        ),
    ]
