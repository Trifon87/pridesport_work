# Generated by Django 3.1.3 on 2020-11-12 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportgoods', '0003_auto_20201112_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gear',
            name='name',
            field=models.CharField(max_length=35),
        ),
        migrations.AlterField(
            model_name='gear',
            name='type',
            field=models.CharField(choices=[('fight', 'fight'), ('fitness', 'fitness'), ('clothing', 'clothing'), ('unknown', 'Unknown')], default='unknown', max_length=35),
        ),
    ]
