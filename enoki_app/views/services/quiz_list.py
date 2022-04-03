from enoki_app.views.db_api.quiz_list import (
    get_quizzes
)

def get_quizzes_from_db(context):
    
    quizzes = get_quizzes()

    context.update({
        'quizzes': quizzes
    })

    return context