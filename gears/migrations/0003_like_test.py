# Generated by Django 3.1.3 on 2020-11-19 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gears', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='test',
            field=models.CharField(default='OK', max_length=2),
        ),
    ]
