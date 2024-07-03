from django.urls import path, include
from learn import views

urlpatterns = [
    path('', views.Index, name='index'),
    path('test/<slug:slug>/', views.take_test, name='take_test'),
    path('test-list/<str:level>', views.test_list, name='test_list'),
]
