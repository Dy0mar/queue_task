from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from queue_task.celery import app
from app_tasks.models import Task
from app_tasks.tasks import save_task


def home(request):
    return render(request, 'tasks/home.html')


@csrf_exempt
def send(request):
    """
    Receives a POST request with data in JSON.
    Request body has “URL” parameter.
    Returns ID of a created task (JSON).
    """
    if request.method == "POST":
        url = request.POST.get('url')
        if url:
            task = save_task.apply_async((url, ))
            i = app.control.inspect()
            data = {
                'task_id': task.id,
                'reserved': i.reserved(),
                'active': i.active()
            }
            return JsonResponse(data=data, safe=False)
    return JsonResponse({}, status=200)


def result(request, task_id):
    """
    Receives a GET request with ID param.
    Returns
    A. If ID is not specified
    Returns last 10 tasks with information on them in JSON format.
    B. If ID is specified
    Information about task with specified ID.
    """
    task = Task.objects.filter(task_id=task_id).first()
    # first is faster than try except block
    if not task:
        data = {
            'task_ids': list(
                Task.objects.values_list('task_id', flat=True)[:10]
            )
        }
        return JsonResponse(data=data)
    return render(request, 'tasks/result.html', {'task': task})
