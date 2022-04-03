from enoki_app.views.services.quiz import (
    get_quiz_from_db
)
from enoki_app.forms import (
    QuizForm
)

def quiz_controller(request, context, id_quiz):

    quiz = get_quiz_from_db(id_quiz)

    print(request.POST)

    form = QuizForm(quiz = quiz)

    context.update({
        'form': form
    })