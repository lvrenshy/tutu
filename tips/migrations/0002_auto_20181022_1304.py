# Generated by Django 2.1.1 on 2018-10-22 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tips', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tips',
            name='spare1',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='tips',
            name='spare2',
            field=models.CharField(max_length=255, null=True),
        ),
    ]