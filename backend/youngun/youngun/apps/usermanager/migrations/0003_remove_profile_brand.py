# Generated by Django 3.0.7 on 2020-07-01 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usermanager', '0002_auto_20200701_1149'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='brand',
        ),
    ]