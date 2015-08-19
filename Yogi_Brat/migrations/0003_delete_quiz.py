# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Yogi_Brat', '0002_contact_quiz'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Quiz',
        ),
    ]
