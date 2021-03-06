from django.urls import path
from sber_backend import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('exercise/all', views.exercise.get_all),
    path('exercise/random', views.exercise.random),
    path('exerciseSession/new', views.exercise_session.new)
] + staticfiles_urlpatterns()


