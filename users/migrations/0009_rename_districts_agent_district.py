# Generated by Django 3.2.12 on 2023-08-12 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_agent_districts'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agent',
            old_name='districts',
            new_name='district',
        ),
    ]
