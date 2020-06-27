# Generated by Django 3.0.7 on 2020-06-27 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0002_auto_20200627_1513'),
        ('usermanager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='brand',
            field=models.ManyToManyField(blank=True, related_name='users', to='usermanager.Brand', verbose_name='brands'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='campaigns',
            field=models.ManyToManyField(blank=True, related_name='profiles', to='campaigns.Campaign', verbose_name='campaigns'),
        ),
    ]
