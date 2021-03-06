from django.urls import path
from .import views
import os

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('another_login/', views.AnotherLoginView.as_view(), name='another_login'),
    path('logout/', views.logout_view, name='logout'),
    path('another_logout/', views.AnotherLogoutView.as_view(), name='another_logout'),
    path('register/', views.register_view, name='register'),
    path('extended_register/', views.another_register_view, name='another_register'),
    
]