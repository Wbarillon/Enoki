from rest_framework import serializers

from enoki_app.models import (
    AnswerChoice,
    AnswerUser,
    Question,
    Quiz
)

class AnswerChoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = AnswerChoice
        fields = '__all__'

class AnswerUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = AnswerUser
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):

    answers_choice = AnswerChoiceSerializer(many = True)

    class Meta:
        model = Question
        fields = [element.name for element in Question._meta.fields] + ['answers_choice']

class QuizSerializer(serializers.ModelSerializer):

    # In order to nest a serializer within a serializer, we need to refer to the foreign key registered among fields. However, we need to refer to the foreignkey by its related_name. As per Django documentation, the default related_name is <modelname_set>.
    # Plus, as we might have several questions in a quiz, they'll be listed. Thus, we need to precise this state with many = True.
    questions = QuestionSerializer(many = True)

    class Meta:
        model = Quiz
        fields = [element.name for element in Quiz._meta.fields] + ['questions']