# Generated by Django 3.1.3 on 2020-11-23 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gears', '0003_like_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gear',
            name='image_url',
            field=models.ImageField(upload_to='gear'),
        ),
    ]