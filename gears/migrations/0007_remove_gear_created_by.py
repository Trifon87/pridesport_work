# Generated by Django 3.1.3 on 2020-12-06 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gears', '0006_remove_gear_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gear',
            name='created_by',
        ),
    ]
