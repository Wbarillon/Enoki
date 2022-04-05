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
    QuizDetail,
    QuizList,
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

test_api = [
    path('quiz_detail/<int:pk>', QuizDetail.as_view()),
    path('quiz_list', QuizList.as_view())
]

router = routers.DefaultRouter()
router.register('answer_choice', AnswerChoiceViewSet)
router.register('answer_user', AnswerUserViewSet)
router.register('question', QuestionViewSet)
router.register('quiz', QuizViewSet)
#router.register('quiz_list', QuizList)
#router.register('quiz_detail', QuizDetail)

urlpatterns = [
    path('', include(webpages_patterns)),
    path('', include(forms_patterns)),
    path('api/', include(router.urls)),
    path('test_api/', include(test_api))
]