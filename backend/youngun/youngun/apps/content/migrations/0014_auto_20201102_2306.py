# Generated by Django 3.0.3 on 2020-11-02 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0013_post_post_engagement'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='total_views',
            field=models.IntegerField(default=0, verbose_name='Total Views (for Video)'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_type',
            field=models.CharField(blank=True, choices=[('p', 'Post'), ('v', 'Video'), ('a', 'Album')], max_length=50, null=True, verbose_name='post_type'),
        ),
    ]
