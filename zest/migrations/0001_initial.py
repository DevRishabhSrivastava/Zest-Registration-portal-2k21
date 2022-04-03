# Generated by Django 3.2.9 on 2021-11-23 17:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import zest.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, default=210000, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter Name', max_length=50, validators=[zest.models.validate_name])),
                ('college_name', models.CharField(choices=[('SRMS CET', 'SRMS CET'), ('SRMS CETR', 'SRMS CETR'), ('SRMS UNNAO', 'SRMS UNNAO'), ('SRMS IMS', 'SRMS IMS'), ('SRMS NURSING', 'SRMS NURSING'), ('OTHER', 'OTHER')], help_text='Select College', max_length=100)),
                ('roll_no', models.IntegerField(unique=True)),
                ('batch', models.CharField(choices=[('2021', '2021'), ('2020', '2020'), ('2019', '2019'), ('2018', '2018'), ('2017', '2017')], help_text='Select Batch', max_length=25)),
                ('course', models.CharField(choices=[('B.Tech.', 'B.Tech.'), ('M.Tech.', 'M.Tech.'), ('B.Pharma', 'B.Pharma'), ('M.Pharma', 'M.Pharma'), ('MBA', 'MBA')], help_text='Select Course', max_length=25)),
                ('branch', models.CharField(choices=[('CSE', 'CSE'), ('IT', 'IT'), ('EC', 'EC'), ('EN', 'EN'), ('ME', 'ME'), ('NA', 'NA')], help_text='Select Branch', max_length=50)),
                ('gender', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')], help_text='Select Gender', max_length=10)),
                ('phone', models.IntegerField(help_text='Enter Mobile No', validators=[zest.models.validate_phone])),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('generated_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='gereted_pid', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, default=310000, primary_key=True, serialize=False, verbose_name='ID')),
                ('college_name', models.CharField(choices=[('SRMS CET', 'SRMS CET'), ('SRMS CETR', 'SRMS CETR'), ('SRMS UNNAO', 'SRMS UNNAO'), ('SRMS IMS', 'SRMS IMS'), ('SRMS NURSING', 'SRMS NURSING'), ('OTHER', 'OTHER')], help_text='Select College', max_length=100)),
                ('generated_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='gereted_tid', to=settings.AUTH_USER_MODEL)),
                ('pid', models.ManyToManyField(blank=True, related_name='pids', to='zest.Pid')),
            ],
        ),
        migrations.CreateModel(
            name='Team_Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(help_text='Enter Event Name', max_length=100)),
                ('event_venue', models.CharField(default=None, help_text='Enter Event Venue', max_length=100)),
                ('event_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('tid', models.ManyToManyField(blank=True, related_name='tid_event', to='zest.Tid')),
            ],
        ),
        migrations.CreateModel(
            name='Individual_Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(help_text='Enter Event Name', max_length=100)),
                ('event_venue', models.CharField(help_text='Enter Event Venue', max_length=100)),
                ('event_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('pid', models.ManyToManyField(blank=True, related_name='pid_event', to='zest.Pid')),
            ],
        ),
    ]
