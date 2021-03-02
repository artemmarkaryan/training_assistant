from django.contrib import admin
from sber_backend.models import Exercise


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    ...