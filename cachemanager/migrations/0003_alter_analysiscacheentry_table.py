# Generated by Django 5.1.4 on 2025-01-05 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cachemanager', '0002_alter_analysiscacheentry_options'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='analysiscacheentry',
            table='analysis_cache',
        ),
    ]
