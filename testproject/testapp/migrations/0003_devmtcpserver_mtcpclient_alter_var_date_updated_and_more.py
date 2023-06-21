# Generated by Django 4.1.7 on 2023-06-21 07:47

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_alter_var_date_updated'),
    ]

    operations = [
        migrations.CreateModel(
            name='Devmtcpserver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_name', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('device_model', models.CharField(blank=True, max_length=255, null=True)),
                ('device_ip', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='testapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='Mtcpclient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('date_updated', models.DateTimeField(blank=True, default=datetime.datetime(2023, 6, 21, 9, 47, 33, 163830))),
                ('regfirst', models.IntegerField(blank=True, null=True)),
                ('regamount', models.IntegerField(blank=True, null=True)),
                ('frequency', models.IntegerField(blank=True, null=True)),
                ('enabled', models.BooleanField(blank=True, null=True)),
                ('server', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='testapp.devmtcpserver')),
            ],
        ),
        migrations.AlterField(
            model_name='var',
            name='date_updated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 6, 21, 9, 47, 33, 163830)),
        ),
        migrations.CreateModel(
            name='Registers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('date_updated', models.DateTimeField(blank=True, default=datetime.datetime(2023, 6, 21, 9, 47, 33, 164868))),
                ('regnumber', models.IntegerField(blank=True, null=True)),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='testapp.mtcpclient')),
            ],
        ),
    ]