# Generated by Django 3.1.3 on 2020-12-08 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pridesport_auth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='date_of_birth',
            field=models.DateTimeField(),
        ),
    ]