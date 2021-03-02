from django.db.models import *


# noinspection PyUnresolvedReferences
class Exercise(Model):
    name = CharField(max_length=128)
    description = TextField()
    muscle_group = ManyToManyField(to='MuscleGroup')


