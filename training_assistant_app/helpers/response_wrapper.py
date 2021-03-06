import json
from typing import Any
from django.http import HttpResponse


class JSONEncoder(json.JSONEncoder):
    def default(self, o: Any) -> str:
        try:
            return json.JSONEncoder.default(self, o)
        except TypeError:
            return str(o)


def json_dump_data(data: Any) -> str:
    return json.dumps(
        {'data': data},
        ensure_ascii=False,
        cls=JSONEncoder
    )


def json_dump_error(message: str) -> str:
    return json.dumps(
        {'error': message},
        ensure_ascii=False,
        cls=JSONEncoder
    )


def wrap_http_data(data: Any) -> HttpResponse:
    return HttpResponse(json_dump_data(data))


def wrap_http_error(message: str, status: int = 400) -> HttpResponse:
    return HttpResponse(
        json_dump_error(message),
        status=status
    )


def wrap_ws_message(message: str) -> dict:
    return {"type": "websocket.send", "text": message}


def wrap_ws_data(data: Any, payload_type: str = None) -> dict:
    payload_type = "MESSAGE" if payload_type is None else payload_type
    payload: str = json.dumps(
        {"type": payload_type, "payload": data},
        ensure_ascii=False,
        cls=JSONEncoder
    )
    return {"type": "websocket.send", "text": payload}

