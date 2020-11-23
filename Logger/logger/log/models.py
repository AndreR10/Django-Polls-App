from logger.settings import STATIC_URL
from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User
# Create your models here.


class Client(models.Model):
    name = models.CharField(max_length=50)

    def __init__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=50)

    def __init__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __init__(self):
        return self.name


class Record(models.Model):
    technician = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
    subject = models.CharField(max_length=100)
    start_date_time = models.DateTimeField(default=timezone.now)
    end_date_time = models.DateTimeField(default=None, blank=True)
    total_hours = models.TimeField()
    service_type = models.OneToOneField(Service, on_delete=models.DO_NOTHING)
    category = models.OneToOneField(Category, on_delete=models.DO_NOTHING)
    description = models.TextField()
    status = models.OneToOneField(default=False)

    def __str__(self):
        return 'Technician: ' + self.technician + '|' + 'Client: ' + self.client + '|' + 'Subject: ' + self.subject + '|' + 'Start at: ' + self.start_date_time + '|' + 'Finished at: ' + self.end_date_time + '|' + 'Total hours: ' + self.total_hours + '|' + 'Service type: ' + self.service_type + '|' + 'Category: ' + self.category + '|' + 'Description: ' + self.description
