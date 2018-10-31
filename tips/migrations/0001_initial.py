# Generated by Django 2.1.1 on 2018-10-22 05:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0004_auto_20181022_1010'),
    ]

    operations = [
        migrations.CreateModel(
            name='tips',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=10000)),
                ('stage', models.CharField(max_length=255)),
                ('tip_name', models.CharField(max_length=140, null=True)),
                ('user_name', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='user.user', to_field='name')),
            ],
        ),
    ]