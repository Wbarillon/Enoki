from enoki_app.models import (
    Quiz
)

def get_quizzes():

    data = Quiz.objects.all()

    return data