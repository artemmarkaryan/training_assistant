from channels.db import database_sync_to_async
from typing import List, Dict
from datetime import datetime, timedelta
from django.db.models import Sum, QuerySet, F

from training_assistant_app.helpers import model_to_dict
from .muscle_group import MUSCLE_GROUP_FIELDS
from ..models.muscle_group import MuscleGroup
from ..models.exercise import Exercise
from ..models.exercise_session import ExerciseSession


@database_sync_to_async
def get_statistics() -> List[Dict]:
    today_exercises: QuerySet = ExerciseSession.objects.filter(
        start__gt=datetime.now() - timedelta(days=1)
    ).select_related(
        'exercise'
    ).select_related(
        'muscle_group'
    ).values(
        'exercise__muscle_group__name'
    ).annotate(
        muscleGroupName=F('exercise__muscle_group__name'),
        experience=Sum('exercise__experience')
    )

    d: dict
    for d in today_exercises:
        del d['exercise__muscle_group__name']

    return list(today_exercises)
