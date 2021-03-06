from django.db.models import *


class ExerciseSession(Model):
    def __str__(self):
        return f'{self.exercise.name} {self.start.strftime("%H:%M")}'

    exercise = ForeignKey('Exercise', on_delete=RESTRICT)
    start = DateTimeField()

