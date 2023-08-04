# Generated by Django 3.2.12 on 2023-08-04 08:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20230803_1209'),
        ('objects', '0002_remove_objectad_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='objectad',
            name='agent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='agent_object', to='users.agent'),
        ),
    ]
