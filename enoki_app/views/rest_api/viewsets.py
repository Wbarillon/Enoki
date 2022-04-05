from rest_framework import generics, viewsets

from enoki_app.models import (
    AnswerChoice,
    AnswerUser,
    Question,
    Quiz
)
from enoki_app.serializers import (
    AnswerChoiceSerializer,
    AnswerUserSerializer,
    QuestionSerializer,
    QuizSerializer
)

class AnswerChoiceViewSet(viewsets.ModelViewSet):
    queryset = AnswerChoice.objects.all()
    serializer_class = AnswerChoiceSerializer

class AnswerUserViewSet(viewsets.ModelViewSet):
    queryset = AnswerUser.objects.all()
    serializer_class = AnswerUserSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all().select_related('id_quiz')
    serializer_class = QuestionSerializer

class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class QuizList(generics.ListCreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class QuizDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer