# Generated by Django 2.2 on 2023-09-15 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_profile_benchmark'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='total_pushups',
            field=models.IntegerField(default=0),
        ),
    ]