from django.urls import path, re_path

from app_tasks import views

urlpatterns = [
    path(r'send/', views.send, name='send'),
    re_path(r'result/(?P<task_id>[\w\-]+)/$', views.result, name='result'),
    path(r'', views.home, name='home'),
]
