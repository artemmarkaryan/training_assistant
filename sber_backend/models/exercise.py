from django.db.models import *


class Exercise(Model):
    def __str__(self):
        return self.name

    name = CharField(max_length=128)
    description = TextField()
    muscle_group = ManyToManyField(to='MuscleGroup')
    duration = IntegerField()
    experience = IntegerField()
