# Generated by Django 3.1.3 on 2020-11-15 05:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20201115_1347'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadfile',
            name='tag',
        ),
    ]