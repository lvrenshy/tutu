# Generated by Django 2.1.1 on 2018-10-22 02:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travelteam', '0003_teaminfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='city',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=255, unique=True)),
                ('city_content', models.CharField(max_length=10000)),
                ('city_id', models.IntegerField(unique=True)),
                ('spare1', models.CharField(max_length=255, null=True)),
                ('spare2', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='teamroute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route', models.CharField(max_length=10000)),
                ('spare1', models.CharField(max_length=255, null=True)),
                ('spare2', models.CharField(max_length=255, null=True)),
                ('city_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travelteam.city', to_field='city_name')),
                ('team_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travelteam.team', to_field='team_name')),
            ],
        ),
    ]
