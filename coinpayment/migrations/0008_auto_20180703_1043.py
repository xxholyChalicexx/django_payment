# Generated by Django 2.0.5 on 2018-07-03 10:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coinpayment', '0007_auto_20180703_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 3, 10, 43, 11, 44291)),
        ),
    ]
