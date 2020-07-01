# Generated by Django 3.0.7 on 2020-07-01 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usermanager', '0001_initial'),
        ('campaigns', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='campaigns', to='usermanager.Brand', verbose_name='Brand'),
        ),
        migrations.CreateModel(
            name='CampaignReport',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('campaigns.campaign',),
        ),
        migrations.CreateModel(
            name='LiveCampaign',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('campaigns.campaign',),
        ),
    ]