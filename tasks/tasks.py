# main/tasks.py

import time

from queue_task.celery import app


@app.task(bind=True)
def some_task():
    time.sleep(5)
