# Generated by Django 2.1.1 on 2018-10-22 05:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20181022_1010'),
        ('question', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_id', models.IntegerField(unique=True)),
                ('content', models.CharField(max_length=10000)),
                ('spare1', models.CharField(max_length=255, null=True)),
                ('spare2', models.CharField(max_length=255, null=True)),
                ('launch_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user', to_field='name')),
            ],
        ),
        migrations.AddField(
            model_name='questionstyle',
            name='spare1',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='questionstyle',
            name='spare2',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='question_style',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question.questionstyle', to_field='style_id'),
        ),
    ]