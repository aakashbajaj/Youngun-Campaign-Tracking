# Generated by Django 3.0.7 on 2020-06-12 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0002_auto_20200611_1800'),
        ('content', '0003_auto_20200611_1800'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name_plural': 'All Posts'},
        ),
        migrations.AddField(
            model_name='post',
            name='campaign',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='campaigns.Campaign', verbose_name='campaign'),
        ),
    ]
