# Generated by Django 3.2 on 2022-03-25 13:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0028_auto_20220325_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upcomingstudentppt',
            name='Time',
            field=models.TimeField(default=datetime.time(18, 31, 0, 314235)),
        ),
        migrations.AlterField(
            model_name='upcomingwebinar',
            name='Time',
            field=models.TimeField(default=datetime.time(18, 31, 0, 313092)),
        ),
    ]
