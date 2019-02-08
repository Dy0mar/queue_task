from django.db import models


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
    task_id = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    status = models.CharField(
        max_length=255, choices=STATUS_CHOICES, default=NEW
    )
    response_length = models.PositiveSmallIntegerField(
        "Response content length", default=0
    )
    response_status = models.PositiveSmallIntegerField(
        "Response content status", default=0
    )
    response_body = models.TextField("Response content body", default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-pk']
