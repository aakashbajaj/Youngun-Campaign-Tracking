# Generated by Django 3.0.8 on 2020-08-18 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0007_auto_20200808_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='alt_google_photo_url',
            field=models.URLField(blank=True, max_length=4000, null=True, verbose_name='Alternate Google Photo URL'),
        ),
        migrations.AlterField(
            model_name='post',
            name='url',
            field=models.URLField(max_length=1000, unique=True, verbose_name='post url'),
        ),
    ]