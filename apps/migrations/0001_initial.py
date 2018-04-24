# Generated by Django 2.0.4 on 2018-04-24 08:14

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestCases',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=200)),
                ('Description', models.CharField(max_length=200)),
                ('Configs', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='TestErrorLogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Data', models.TextField()),
                ('test_cases', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.TestCases')),
            ],
        ),
        migrations.CreateModel(
            name='TestIoLogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Timestamp', models.IntegerField()),
                ('Percentile', models.FloatField()),
                ('Wr_iops', models.FloatField()),
                ('Wr_throughput', models.FloatField()),
                ('Wr_latency', models.FloatField()),
                ('Rd_iops', models.FloatField()),
                ('Rd_throughput', models.FloatField()),
                ('Rd_latency', models.FloatField()),
                ('test_cases', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.TestCases')),
            ],
        ),
        migrations.CreateModel(
            name='TestSmartLogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Timestamp', models.DateTimeField()),
                ('Data_units_read', models.IntegerField()),
                ('test_cases', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.TestCases')),
            ],
        ),
    ]
