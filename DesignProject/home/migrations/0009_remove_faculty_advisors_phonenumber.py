# Generated by Django 3.2 on 2022-02-04 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_faculty_advisors_phonenumber'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faculty_advisors',
            name='phoneNumber',
        ),
    ]
