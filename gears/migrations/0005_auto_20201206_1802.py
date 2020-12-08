# Generated by Django 3.1.3 on 2020-12-06 16:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gears', '0004_auto_20201123_1045'),
    ]

    operations = [
        migrations.AddField(
            model_name='gear',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gear',
            name='likes',
            field=models.IntegerField(blank=True, default=1),
            preserve_default=False,
        ),
    ]
