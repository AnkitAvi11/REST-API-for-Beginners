# Generated by Django 3.1.4 on 2020-12-16 05:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0004_auto_20201206_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 16, 5, 51, 15, 170385, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='question',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 16, 5, 51, 15, 170385, tzinfo=utc)),
        ),
    ]
