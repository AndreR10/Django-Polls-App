# Generated by Django 3.1.3 on 2020-11-23 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0004_auto_20201123_1843'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Technician',
        ),
    ]