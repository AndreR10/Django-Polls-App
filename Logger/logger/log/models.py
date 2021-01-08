from logger.settings import STATIC_URL
from django.db import models
from django.utils import timezone
from datetime import date, time

from django.contrib.auth.models import User
# Create your models here.


class Client(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Log(models.Model):
    technician = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
    subject = models.CharField(max_length=100)
    date = models.DateField(default=None)
    start_time = models.TimeField(default=None)
    end_time = models.TimeField(default=None)
    total_hours = models.PositiveIntegerField(blank=True, null=True)
    service_type = models.ForeignKey(Service, on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    description = models.TextField(max_length=500)
    status = models.ForeignKey(Status, on_delete=models.DO_NOTHING)
