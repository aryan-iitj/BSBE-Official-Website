# Generated by Django 3.2 on 2022-02-04 07:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20220204_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty_advisors',
            name='phoneNumber',
            field=models.CharField(blank=True, max_length=16, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{8,15}$')]),
        ),
    ]