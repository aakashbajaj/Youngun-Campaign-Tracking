# Generated by Django 3.0.7 on 2020-07-05 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usermanager', '0006_auto_20200704_1912'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffprofile',
            name='added_by',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='invited_users', to='usermanager.StaffProfile', verbose_name='Added By'),
        ),
    ]
