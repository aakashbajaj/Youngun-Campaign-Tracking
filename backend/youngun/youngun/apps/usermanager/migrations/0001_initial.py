# Generated by Django 3.0.7 on 2020-06-27 15:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('campaigns', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, default='', max_length=255, verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, default='', max_length=255, verbose_name='Last Name')),
                ('brand', models.ManyToManyField(related_name='users', to='usermanager.Brand', verbose_name='brands')),
                ('campaigns', models.ManyToManyField(related_name='profiles', to='campaigns.Campaign', verbose_name='campaigns')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='')),
            ],
        ),
        migrations.AddField(
            model_name='brand',
            name='organisation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='usermanager.Organisation', verbose_name='organisation'),
        ),
    ]