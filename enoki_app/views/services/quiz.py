import ast

from enoki_app.forms import (
    AnswerUserModelForm,
    QuizForm
)
from enoki_app.models import (
    AnswerUser
)
from enoki_app.views.db_api.quiz import (
    get_quiz
)
from enoki_project.utils import save_django_object

def get_quiz_from_db(context, id_quiz):

    quiz = get_quiz(id_quiz)

    # Valid entry to populate form
    data = {
        'question_1': [6],
        'question_2': [9]
    }

    form = QuizForm(quiz = quiz)

    context.update({
        'form': form
    })

    return context, quiz

def save_quiz_answers(request, quiz):

    #À faire :
    #- sauvegarder les données dans la table AnswerUser sous forme json
    #- enregistrer l'id du questionnaire en plus des réponses
    #- tester si il est possible de construire un formulaire rempli avec les réponses du json

    form = QuizForm(request.POST, quiz = quiz)

    print(request.POST)

    if form.is_valid():

        print(form.cleaned_data)

        for value in form.cleaned_data.values():
            data = {
                'id_user': request.user.id,
                'id_answer_choice': int(ast.literal_eval(value)[0])
            }

            answer_user_model_form = AnswerUserModelForm(data)
            del data

            if answer_user_model_form.is_valid():

                print(answer_user_model_form.cleaned_data)

                #save_django_object(AnswerUser(), answer_user_model_form.cleaned_data)