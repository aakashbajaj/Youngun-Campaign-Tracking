# Generated by Django 3.0.7 on 2020-07-01 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usermanager', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='organisation',
        ),
        migrations.DeleteModel(
            name='Organisation',
        ),
    ]
