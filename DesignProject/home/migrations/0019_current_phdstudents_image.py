# Generated by Django 3.2 on 2022-02-04 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_current_phdstudents'),
    ]

    operations = [
        migrations.AddField(
            model_name='current_phdstudents',
            name='image',
            field=models.ImageField(default=1, upload_to='images/'),
            preserve_default=False,
        ),
    ]
