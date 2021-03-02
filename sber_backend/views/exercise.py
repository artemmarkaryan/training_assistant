from django.http.request import HttpRequest
from training_assistant_app.helpers import json_wrapper
from sber_backend import db_interface


def get_all(_: HttpRequest):
    return json_wrapper.wrap_data(
        db_interface.exercise.get_all()
    )
