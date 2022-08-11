# Generated by Django 3.2 on 2022-02-04 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_current_phdstudents_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Graduated_PhdStudents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('GraduationYear', models.IntegerField()),
                ('Supervisor', models.CharField(max_length=900)),
                ('ResearchArea', models.CharField(max_length=900)),
                ('ThesisTitle', models.CharField(max_length=900)),
                ('CurrentPosition', models.CharField(max_length=900)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
