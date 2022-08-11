# Generated by Django 3.2 on 2022-05-06 10:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0050_auto_20220506_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicationlist',
            name='Title',
            field=models.CharField(max_length=400, unique=b'I01\n'),
        ),
        migrations.AlterField(
            model_name='upcomingstudentppt',
            name='Time',
            field=models.TimeField(default=datetime.time(16, 25, 59, 280297)),
        ),
        migrations.AlterField(
            model_name='upcomingwebinar',
            name='Time',
            field=models.TimeField(default=datetime.time(16, 25, 59, 280297)),
        ),
    ]
