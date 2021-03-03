from ..models.exercise import Exercise
from training_assistant_app.helpers import model_to_dict
from .fields.exercise import EXERCISE_FIELDS
from .fields.muscle_group import MUSCLE_GROUP_FIELDS


def get_all():
    all_exercises = []
    for ex in Exercise.objects.all():

        exercise_dict: dict = model_to_dict.convert(ex, EXERCISE_FIELDS)
        exercise_dict.update(muscleGroups=[
            model_to_dict.convert(mg, MUSCLE_GROUP_FIELDS)
            for mg in ex.muscle_group.all()
        ])
        all_exercises.append(exercise_dict)
    return all_exercises