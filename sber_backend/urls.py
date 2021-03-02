from django.urls import path
from sber_backend import views

urlpatterns = [
    path('exercise/all', views.exercise.get_all),
]


