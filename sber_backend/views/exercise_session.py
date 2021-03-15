from django.http import HttpRequest
from .. import db_interface
from ..models import Exercise
from training_assistant_app.helpers import response_wrapper


def new(request: HttpRequest):
    try:
        exercise_id = request.GET.get(key="exerciseId")
        new_exercise_session_id = db_interface.exercise_session.new(
            exercise_id
        )
        return response_wrapper.wrap_http_data(
            {"newExerciseId": new_exercise_session_id}
        )
    except Exercise.DoesNotExist:
        return response_wrapper.wrap_http_error(
            "Не найдено упражнение с таким id"
        )
