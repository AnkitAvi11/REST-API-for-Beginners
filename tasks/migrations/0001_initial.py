# Generated by Django 3.1.4 on 2020-12-16 05:51

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('completion_date', models.DateField(default=datetime.datetime(2020, 12, 16, 5, 51, 15, 170385, tzinfo=utc))),
                ('status', models.BooleanField(default=False)),
                ('posted_on', models.DateTimeField(default=datetime.datetime(2020, 12, 16, 5, 51, 15, 170385, tzinfo=utc))),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
