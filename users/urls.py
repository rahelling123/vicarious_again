"""Defines urls for the users"""

from django.conf.urls import url
from django.http import request
from django.urls import path
from django.contrib.auth.views import LoginView
from users.views import signup, logout_view, login_view, test_model_view, dashboard, visitor

app_name = 'users'
urlpatterns = [
    path('login/', login_view, name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', logout_view, name='logout'),
    path('testform/', test_model_view, name='test_model_view'),
    path('dashboard/<int:user_id>', dashboard, name='dashboard'),
    path('visitor/<int:user_id>', visitor, name='visitor'),
]

