from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.tasks, name='tasks'),
    path('complete/<int:task_id>/', views.completeTask, name='complete_task'),
    path('upcoming/', views.upcomingTasks, name='upcoming tasks'),
    path('missed/', views.missedTasks, name='missedtask'),
    path('add/', views.addtask, name='addtask'),    
]