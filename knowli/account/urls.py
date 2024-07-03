from django.urls import path, include
from django.contrib.auth import views
from account import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register')
]
