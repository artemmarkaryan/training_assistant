from ..models import ExerciseSession, Exercise


def new(exercise_id: id) -> int:
    new_session = ExerciseSession(exercise=Exercise.objects.get(id=exercise_id))
    new_session.save()
    return new_session.id
