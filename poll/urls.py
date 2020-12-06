from django.urls import path, re_path

from . import views

urlpatterns = [
    path('posts/', views.questions, name='questions'),
    path('choices/', views.choices, name='choices')
]