import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


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
            return JsonResponse({}, status=200)
    return JsonResponse({}, status=200)


def result(request, id=None):
    """
    Receives a GET request with ID param.
    Returns
    A. If ID is not specified
    Returns last 10 tasks with information on them in JSON format.
    B. If ID is specified
    Information about task with specified ID.
    """

    pass