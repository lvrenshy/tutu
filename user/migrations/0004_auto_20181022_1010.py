# Generated by Django 2.1.1 on 2018-10-22 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_userinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='tel',
            field=models.IntegerField(null=True, unique=True),
        ),
    ]
