from django.contrib import admin
from sber_backend.models import MuscleGroup


@admin.register(MuscleGroup)
class MuscleGroupAdmin(admin.ModelAdmin):
    ...
