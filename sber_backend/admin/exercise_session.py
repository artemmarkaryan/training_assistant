from django.contrib import admin
from sber_backend.models import ExerciseSession


@admin.register(ExerciseSession)
class ExerciseSessionAdmin(admin.ModelAdmin):
    ...