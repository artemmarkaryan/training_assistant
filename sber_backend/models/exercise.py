from django.db.models import *


class Exercise(Model):
    name = CharField(max_length=128)
    description = TextField()
    muscle_group = ManyToManyField(to='MuscleGroup')
    duration = IntegerField()
    experience = IntegerField()


