from django.db.models import *


# noinspection PyUnresolvedReferences
class MuscleGroup(Model):
    def __str__(self):
        return self.name

    name = CharField(max_length=128)
    description = TextField()


