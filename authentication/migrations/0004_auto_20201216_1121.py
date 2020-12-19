# Generated by Django 3.1.4 on 2020-12-16 05:51

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authentication', '0003_auto_20201206_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='joined_on',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 16, 5, 51, 15, 170385, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]