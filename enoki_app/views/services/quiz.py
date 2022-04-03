from enoki_app.views.db_api.quiz import (
    get_quiz
)

def get_quiz_from_db(id_quiz):

    quiz = get_quiz(id_quiz)

    return quiz