# Generated by Django 2.2 on 2023-09-15 20:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pushups', '0003_auto_20230915_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='benchmarktest',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 9, 15, 20, 9, 38, 196851, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='workout',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 9, 15, 20, 9, 38, 197116, tzinfo=utc)),
        ),
    ]