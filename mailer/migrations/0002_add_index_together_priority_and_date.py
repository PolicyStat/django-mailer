# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailer', '0001_initial'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='message',
            index_together=set([('priority', 'when_added')]),
        ),
    ]
