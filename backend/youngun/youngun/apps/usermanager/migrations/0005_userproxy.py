# Generated by Django 3.0.7 on 2020-07-04 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20200704_1019'),
        ('usermanager', '0004_auto_20200704_0904'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProxy',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('authentication.user',),
        ),
    ]
