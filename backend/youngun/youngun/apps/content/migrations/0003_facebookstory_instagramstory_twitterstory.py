# Generated by Django 3.0.7 on 2020-07-01 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_auto_20200701_1743'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacebookStory',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('content.story',),
        ),
        migrations.CreateModel(
            name='InstagramStory',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('content.story',),
        ),
        migrations.CreateModel(
            name='TwitterStory',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('content.story',),
        ),
    ]