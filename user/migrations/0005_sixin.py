# Generated by Django 2.1.1 on 2018-10-29 00:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20181022_1010'),
    ]

    operations = [
        migrations.CreateModel(
            name='sixin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=10000)),
                ('userid', models.CharField(max_length=255, null=True)),
                ('spare1', models.CharField(max_length=255, null=True)),
                ('spare2', models.CharField(max_length=255, null=True)),
                ('uptime', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user', to_field='name')),
            ],
        ),
    ]
