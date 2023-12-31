# Generated by Django 4.2 on 2023-06-10 18:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jobwebsite", "0009_alter_profile_age"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="email",
        ),
        migrations.RemoveField(
            model_name="profile",
            name="first_name",
        ),
        migrations.RemoveField(
            model_name="profile",
            name="last_name",
        ),
        migrations.RemoveField(
            model_name="profile",
            name="username",
        ),
        migrations.AlterField(
            model_name="profile",
            name="birthdate",
            field=models.DateField(default=datetime.date(2023, 6, 10)),
        ),
    ]
