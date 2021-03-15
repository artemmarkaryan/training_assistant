from typing import *
from django.db.models import QuerySet, Model, F as original_name

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


def query_to_dict(query, fields: FieldNameMapping) -> QuerySet:
    unchanged_fields = []
    renamed_fields = {}
    for f in fields:
        if isinstance(f, str):
            unchanged_fields.append(f)
        else:
            renamed_fields[f[1]] = original_name(f[0])
    return query.values(*unchanged_fields, **renamed_fields)
