from django.urls import path
from StudentApp import views

urlpatterns = [
    path('students/', views.studentApi, name='Student'),
]