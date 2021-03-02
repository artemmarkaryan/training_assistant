from typing import *
from django.db.models import Model

FieldNameMapping = Iterable[Union[str, tuple]]


def convert(
        model_instance: Model,
        fields: FieldNameMapping
) -> Dict[str, Any]:
    result_dict = {}

    for field in fields:
        if type(field) is str:
            result_dict[field] = model_instance.__getattribute__(field)
        else:
            result_dict[field[0]] = model_instance.__getattribute__(field[1])

    return result_dict
