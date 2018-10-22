# Generated by Django 2.1.1 on 2018-10-18 16:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fest_app', '0002_events'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoboSoccer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=20)),
                ('last_name', models.CharField(default='', max_length=20)),
                ('email', models.EmailField(default='', max_length=40)),
                ('roll', models.CharField(default='', max_length=10)),
                ('phone', models.CharField(default='', max_length=10)),
                ('branch', models.CharField(default='', max_length=10)),
                ('section', models.CharField(default='', max_length=2)),
                ('year', models.CharField(default='', max_length=10)),
                ('event_id', models.CharField(default='', max_length=5)),
                ('event_name', models.CharField(default='', max_length=20)),
                ('team_name', models.CharField(default='', max_length=20)),
                ('number_of_members', models.CharField(default='', max_length=20)),
                ('member_1', models.CharField(default='', max_length=20)),
                ('member_2', models.CharField(default='', max_length=20)),
                ('member_3', models.CharField(default='', max_length=20)),
                ('member_4', models.CharField(default='', max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WaterRocketry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=20)),
                ('last_name', models.CharField(default='', max_length=20)),
                ('email', models.EmailField(default='', max_length=40)),
                ('roll', models.CharField(default='', max_length=10)),
                ('phone', models.CharField(default='', max_length=10)),
                ('branch', models.CharField(default='', max_length=10)),
                ('section', models.CharField(default='', max_length=2)),
                ('year', models.CharField(default='', max_length=10)),
                ('event_id', models.CharField(default='', max_length=5)),
                ('event_name', models.CharField(default='', max_length=20)),
                ('team_name', models.CharField(default='', max_length=20)),
                ('number_of_members', models.CharField(default='', max_length=20)),
                ('member_1', models.CharField(default='', max_length=20)),
                ('member_2', models.CharField(default='', max_length=20)),
                ('member_3', models.CharField(default='', max_length=20)),
                ('member_4', models.CharField(default='', max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Events',
        ),
    ]
