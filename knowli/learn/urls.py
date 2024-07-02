from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.Index, name='index'),
    path('test-dodawanie/', views.addition_test, name='test_dodawanie'),
    path('wyniki/', views.test_results, name="wyniki_testow")
]
