from enoki_app.views.services.quiz_list import (
    get_quizzes_from_db
)

def quiz_list_controller(request, context):

    context = get_quizzes_from_db(context)