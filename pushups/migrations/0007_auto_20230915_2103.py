# Generated by Django 2.2 on 2023-09-15 21:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pushups', '0006_auto_20230915_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='benchmarktest',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 9, 15, 21, 3, 9, 648698, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='workout',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 9, 15, 21, 3, 9, 648958, tzinfo=utc)),
        ),
    ]