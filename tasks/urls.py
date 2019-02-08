from django.urls import path, re_path

from tasks import views

urlpatterns = [
    path(r'send/', views.send, name='send'),
    path(r'result/', views.result, name='result-list'),
    re_path(r'result/(?P<task_id>\s+)', views.result, name='result-id'),
    path(r'', views.home, name='home'),
]
