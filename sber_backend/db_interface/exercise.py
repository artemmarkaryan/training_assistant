import random
from datetime import datetime, timedelta
from django.db.models import QuerySet
from typing import List
from ..models.exercise import Exercise
from ..models.muscle_group import MuscleGroup
from training_assistant_app.helpers import model_to_dict
from .fields.exercise import EXERCISE_FIELDS
from .fields.muscle_group import MUSCLE_GROUP_FIELDS


class ExerciseIdCache:
    TIMEOUT_MIN = 10
    last_update: datetime = None
    __cache: List[int] = []

    def __init__(self):
        self.update_ids()

    def __cache_is_relevant(self) -> bool:
        if self.last_update is None:
            return False
        if (self.last_update - datetime.now()) < timedelta(
                minutes=self.TIMEOUT_MIN):
            return False

    def update_ids(self):
        if not self.__cache_is_relevant():
            self.__cache = Exercise.objects.all().values_list('id', flat=True)
            self.last_update = datetime.now()

    @property
    def cache(self) -> List[int]:
        self.update_ids()
        return self.__cache


exercise_id_cache = ExerciseIdCache()


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


def get_random(excluded_ids: List[int]):
    exercise_id = random.choice(list(
        set(exercise_id_cache.cache).difference(set(excluded_ids))
    ))
    exercise_instance: Exercise = Exercise.objects.filter(id=exercise_id)
    exercise_query: QuerySet[Exercise] = model_to_dict.query_to_dict(
        exercise_instance, EXERCISE_FIELDS
    )
    exercise_dict = exercise_query.get(id=exercise_id)
    exercise_dict['muscleGroups'] = list(MuscleGroup.objects.filter(
        exercise__in=exercise_instance
    ).values_list('name', flat=True))
    return exercise_dict
