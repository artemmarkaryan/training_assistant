from django.contrib import admin
from sber_backend.models import TrainingSession


@admin.register(TrainingSession)
class TrainingSessionAdmin(admin.ModelAdmin):
    ...