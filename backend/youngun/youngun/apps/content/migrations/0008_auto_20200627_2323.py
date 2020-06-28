# Generated by Django 3.0.7 on 2020-06-27 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0007_auto_20200627_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='visibility',
            field=models.CharField(choices=[('public', 'Public'), ('private', 'Private')], default='public', max_length=50, verbose_name='post visibility'),
        ),
    ]
