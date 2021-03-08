from channels.db import database_sync_to_async
from typing import List, Dict, Coroutine
from datetime import datetime, timedelta
from django.db.models import Sum, QuerySet, F

from training_assistant_app.helpers import model_to_dict
from .muscle_group import MUSCLE_GROUP_FIELDS
from ..models.muscle_group import MuscleGroup
from ..models.exercise import Exercise
from ..models.exercise_session import ExerciseSession


@database_sync_to_async
def get_daily_statistics():
    today_exercise_sessions: QuerySet = ExerciseSession.objects.filter(
        start__gt=datetime.now() - timedelta(days=1)
    ).select_related('exercise')

    per_muscle_group = {}
    exercise_session_count = len(today_exercise_sessions)
    for muscle_group in MuscleGroup.objects.all():

        per_muscle_group[muscle_group.name] = sum(
            [
                ex_sess.exercise.experience for ex_sess in today_exercise_sessions
                if muscle_group in ex_sess.exercise.muscle_group.all()
            ]
        )

    return {
        'perMuscleGroup': per_muscle_group,
        'exerciseSessions': exercise_session_count
    }
