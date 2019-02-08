import time
import requests
from celery import shared_task

from app_tasks.models import Task


@shared_task(bind=True)
def save_task(self, url):
    print('task id - ', self.request.id)

    task = Task.objects.create(
        task_id=self.request.id,
        url=url,
        response_body=''
    )
    time.sleep(10)

    task.status = Task.PENDING
    task.save()
    time.sleep(10)
    try:
        r = requests.get(url)
    except requests.ReadTimeout:
        task.status = Task.ERROR
        task.save()
    else:
        task.status = Task.COMPLETED
        task.response_length = len(r.content)
        task.response_status = r.status_code
        task.response_body = r.content
        task.save()
    time.sleep(10)
