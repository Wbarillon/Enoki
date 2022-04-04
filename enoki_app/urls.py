from django.urls import include, path
from rest_framework import routers

from enoki_app.views.index import (
    authentication,
    home,
    quiz,
    quiz_list
)
from enoki_app.views.rest_api.viewsets import (
    AnswerChoiceViewSet,
    AnswerUserViewSet,
    QuestionViewSet,
    QuizViewSet
)

webpages_patterns = [
    path('', home, name = 'home'),
    path('quiz_list', quiz_list, name = 'quiz_list')
]

forms_patterns = [
    path('authentication', authentication, name = 'authentication'),
    path('quiz/<int:id_quiz>', quiz, name = 'quiz')
]

router = routers.DefaultRouter()
router.register('answer_choice', AnswerChoiceViewSet)
router.register('answer_user', AnswerUserViewSet)
router.register('question', QuestionViewSet)
router.register('quiz', QuizViewSet)

urlpatterns = [
    path('', include(webpages_patterns)),
    path('', include(forms_patterns)),
    path('api/', include(router.urls))
]