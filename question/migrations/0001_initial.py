# Generated by Django 2.1.1 on 2018-10-22 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='questionstyle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('style_id', models.IntegerField(unique=True)),
                ('style_name', models.CharField(max_length=30)),
            ],
        ),
    ]
