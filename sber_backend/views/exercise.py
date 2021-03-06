from django.http.request import HttpRequest
from training_assistant_app.helpers import response_wrapper
from sber_backend import db_interface


def get_all(_: HttpRequest):
    return response_wrapper.wrap_http_data(
        db_interface.exercise.get_all()
    )
