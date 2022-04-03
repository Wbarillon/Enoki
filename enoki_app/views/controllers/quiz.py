from enoki_app.views.services.quiz import (
    get_quiz_from_db,
    save_quiz_answers
)

def quiz_controller(request, context, id_quiz):

    context, quiz = get_quiz_from_db(context, id_quiz)

    if request.method == 'POST':

        save_quiz_answers(request, quiz)