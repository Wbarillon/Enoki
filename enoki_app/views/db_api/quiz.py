import json

from django.db import connection

def get_quiz(id_quiz):

    query = '''
        select jsonb_agg(quiz) as quiz
        from (
            select
                eaq.question,
                array(
                    select json_build_object(eaa.id, eaa.answer_choice)
                    from enoki_app_answerchoice as eaa
                    where eaa.id_question_id = eaq.id
                    order by eaa.id
                ) as answers_choice
            from enoki_app_question as eaq
            where eaq.id_quiz_id = %(id_quiz)s
        ) as quiz
    '''

    query2 = '''
        select jsonb_agg(quiz) as quiz
        from (
            select
                eaq.question,
                array(
                    select eaa.answer_choice
                    from enoki_app_answerchoice as eaa
                    where eaa.id_question_id = eaq.id
                    order by eaa.id
                ) as answers_choice
            from enoki_app_question as eaq
            where eaq.id_quiz_id = %(id_quiz)s
        ) as quiz
    '''

    with connection.cursor() as cursor:
        cursor.execute(
            query,
            {
                'id_quiz': id_quiz
            }
        )

        data = cursor.fetchall()[0][0]
        data = json.loads(data)

    return data