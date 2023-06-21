from django.db import models
from datetime import datetime

# Create your models here.


class AlembicVersion(models.Model):
    version_num = models.CharField(primary_key=True, max_length=255)



class Device(models.Model):
    device_name = models.CharField(blank=True, null=True, max_length=255)
    date = models.DateTimeField(blank=True, null=True)
    device_model = models.CharField(blank=True, null=True, max_length=255)
    device_ip = models.CharField(blank=True, null=True, max_length=255)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)



    def __str__(self):
        return f"{self.device_name} ({self.device_ip})"


class Note(models.Model):
    note = models.CharField(blank=True, null=True, max_length=255)
    sec = models.IntegerField(blank=True, null=True)
    data = models.CharField(blank=True, null=True, max_length=255)
    date = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)



class User(models.Model):
    email = models.CharField(blank=True, null=True, max_length=255)
    password = models.CharField(blank=True, null=True, max_length=255)
    first_name = models.CharField(blank=True, null=True, max_length=255)


    def __str__(self):
        return f"{self.first_name} ({self.email})"


class Value(models.Model):
    date_created = models.DateTimeField(blank=True, null=True)
    var = models.ForeignKey('Var', models.DO_NOTHING, blank=True, null=True)
    value = models.TextField(blank=True, null=True)  # This field type is a guess.


class Var(models.Model):
    value_name = models.CharField(blank=True, null=True, max_length=255)
    date = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    device = models.ForeignKey(Device, models.DO_NOTHING, blank=True, null=True)
    date_updated = models.DateTimeField(blank=True, null=False, default=datetime.now())
    frequency = models.IntegerField(blank=True, null=True)
    enabled = models.BooleanField(blank=True, null=True)

class Devmtcpserver(models.Model):
    device_name = models.CharField(blank=True, null=True, max_length=255)
    date = models.DateTimeField(blank=True, null=True)
    device_model = models.CharField(blank=True, null=True, max_length=255)
    device_ip = models.CharField(blank=True, null=True, max_length=255)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)

class Mtcpclient(models.Model):
    name = models.CharField(blank=True, null=True, max_length=255)
    date = models.DateTimeField(blank=True, null=True)
    server = models.ForeignKey(Devmtcpserver, models.DO_NOTHING, blank=True, null=True)
    date_updated = models.DateTimeField(blank=True, null=False, default=datetime.now())
    regfirst = models.IntegerField(blank=True, null=True)
    regamount = models.IntegerField(blank=True, null=True)
    frequency = models.IntegerField(blank=True, null=True)
    enabled = models.BooleanField(blank=True, null=True)

class Registers(models.Model):
    name = models.CharField(blank=True, null=True, max_length=255)
    date = models.DateTimeField(blank=True, null=True)
    client = models.ForeignKey(Mtcpclient, models.DO_NOTHING, blank=True, null=True)
    date_updated = models.DateTimeField(blank=True, null=False, default=datetime.now())
    regnumber = models.IntegerField(blank=True, null=True)