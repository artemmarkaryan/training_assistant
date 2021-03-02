from typing import Iterable, Union, NewType
from django.db.models import Model
from training_assistant_app.helpers import model_to_dict


def get_all(model: [Model], fields: model_to_dict.FieldNameMapping):
    return [model_to_dict.convert(obj, fields) for obj in model.objects.all()]
