# Generated by Django 2.1.1 on 2018-10-22 02:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travelteam', '0002_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='teaminfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_number', models.IntegerField(null=True)),
                ('starttime', models.CharField(max_length=60)),
                ('endtime', models.CharField(max_length=60)),
                ('introduce', models.CharField(max_length=100)),
                ('start_stage', models.CharField(max_length=200)),
                ('end_stage', models.CharField(max_length=200)),
                ('spare1', models.CharField(max_length=255, null=True)),
                ('spare2', models.CharField(max_length=255, null=True)),
                ('team_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travelteam.team', to_field='team_name')),
            ],
        ),
    ]
