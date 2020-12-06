from django.urls import path, re_path

from . import views

urlpatterns = [
    path('signup/', views.signupUser, name='signup'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout')
]