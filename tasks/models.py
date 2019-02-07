from django.db import models

# Create your models here.


class Task(models.Model):
    NEW = 1
    PENDING = 2
    COMPLETED = 3
    ERROR = 4

    STATUS_CHOICES = (
        (NEW, 'NEW'),
        (PENDING, 'PENDING'),
        (COMPLETED, 'COMPLETED'),
        (ERROR, 'ERROR'),
    )
    url = models.CharField(max_length=255)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES)
    response_length = models.PositiveSmallIntegerField(
        "Response content length", default=0
    )
    response_status = models.PositiveSmallIntegerField(
        "Response content status", default=0
    )
    response_body = models.TextField("Response content body")
