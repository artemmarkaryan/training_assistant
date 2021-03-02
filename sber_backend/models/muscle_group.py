from django.db.models import *


# noinspection PyUnresolvedReferences
class MuscleGroup(Model):
    name = CharField(max_length=128)
    description = TextField()


