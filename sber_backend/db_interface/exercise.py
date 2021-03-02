from ..models.exercise import Exercise
from ..db_interface import common

EXERCISE_FIELDS = (
    'name',
    'description',
    ('muscle_group', 'muscleGroup'),
    'duration',
    'experience'
)


def get_all():
    return common.get_all(Exercise, EXERCISE_FIELDS)
