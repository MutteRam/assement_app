from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [

    path('', views.home, name='home'),
    path('assessment/', views.assessment, name='assessment'),
    path('assessment/run-code/', views.run_code, name='run_code'),
]