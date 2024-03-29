# Generated by Django 3.0.3 on 2021-01-22 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0011_auto_20210118_0907'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='fb_engagement',
            field=models.IntegerField(default=0, verbose_name='fb_engagement'),
        ),
        migrations.AddField(
            model_name='campaign',
            name='fb_reach',
            field=models.IntegerField(default=0, verbose_name='fb_reach'),
        ),
        migrations.AddField(
            model_name='campaign',
            name='in_engagement',
            field=models.IntegerField(default=0, verbose_name='in_engagement'),
        ),
        migrations.AddField(
            model_name='campaign',
            name='in_reach',
            field=models.IntegerField(default=0, verbose_name='in_reach'),
        ),
        migrations.AddField(
            model_name='campaign',
            name='tw_engagement',
            field=models.IntegerField(default=0, verbose_name='tw_engagement'),
        ),
        migrations.AddField(
            model_name='campaign',
            name='tw_reach',
            field=models.IntegerField(default=0, verbose_name='tw_reach'),
        ),
    ]
