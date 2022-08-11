# Generated by Django 3.2 on 2022-01-29 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_rename_people_faculty_advisors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty_advisors',
            name='FacultyType',
            field=models.CharField(blank=True, choices=[('RegularFaculty', 'RegularFaculty'), ('YoungFacultyAssociates', 'YoungFacultyAssociates'), ('GuestFaculty', 'GuestFaculty'), ('AdjunctFaculty', 'AdjunctFaculty'), ('ScholarsinResidence', 'ScholarsinResidence'), ('Advisors', 'Advisors')], max_length=60),
        ),
    ]
