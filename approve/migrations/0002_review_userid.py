# Generated by Django 2.1.1 on 2018-10-25 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('approve', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='userid',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
