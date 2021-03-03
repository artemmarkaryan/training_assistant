from django.contrib import admin
from sber_backend.models import Exercise


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    filter_horizontal = ['muscle_group']