# Generated by Django 3.0.3 on 2021-02-02 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0017_auto_20210130_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='upload_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Upload DateTime'),
        ),
    ]
