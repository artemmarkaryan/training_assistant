from django.db.models import *


class TrainingSession(Model):
    def __str__(self):
        return self.exercise.name

    exercise = ForeignKey('Exercise', on_delete=RESTRICT)
    start = DateTimeField()
    end = DateTimeField()
