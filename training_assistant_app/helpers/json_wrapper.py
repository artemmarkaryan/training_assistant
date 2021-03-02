import json
from typing import Any
from django.http import HttpResponse


class JSONEncoder(json.JSONEncoder):
    def default(self, o: Any) -> Any:
        try:
            return json.JSONEncoder.default(self, o)
        except TypeError:
            return str(o)


def wrap_data(data: dict) -> HttpResponse:
    return HttpResponse(
        json.dumps(
            {'data': data},
            ensure_ascii=False,
            cls=JSONEncoder
        )
    )


def wrap_error(message: str, status: int = 400) -> HttpResponse:
    return HttpResponse(
        json.dumps(
            {'error': message},
            ensure_ascii=False,
            cls=JSONEncoder
        ),
        status=status
    )
