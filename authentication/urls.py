from django.urls import path, re_path

from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', views.signupUser, name='signup'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('user/', views.getUser, name='getuser'),
    path('validate/', views.validateUser, name='validateuser'),

    #   auth views for password reset
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),

    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    #   profile setting
    path('updateuser/', views.updateUser, name='update user')

]