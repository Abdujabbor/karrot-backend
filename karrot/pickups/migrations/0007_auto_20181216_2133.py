# Generated by Django 2.1.4 on 2018-12-16 21:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pickups', '0006_auto_20181216_2130'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pickupdate',
            old_name='done_and_processed',
            new_name='feedback_possible',
        ),
        migrations.RenameField(
            model_name='pickupdate',
            old_name='deleted',
            new_name='is_disabled',
        ),
        migrations.RemoveField(
            model_name='pickupdate',
            name='is_date_changed',
        ),
        migrations.RemoveField(
            model_name='pickupdate',
            name='is_description_changed',
        ),
        migrations.RemoveField(
            model_name='pickupdate',
            name='is_max_collectors_changed',
        ),
        migrations.AddField(
            model_name='pickupdate',
            name='last_changed_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pickups_changed', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='pickupdateseries',
            name='last_changed_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='changed_series', to=settings.AUTH_USER_MODEL),
        ),
    ]
