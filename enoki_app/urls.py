from django.urls import include, path

from enoki_app.views.index import (
    authentication,
    home,
    quiz,
    quiz_list
)

webpages_patterns = [
    path('', home, name = 'home'),
    path('quiz_list', quiz_list, name = 'quiz_list')
]

forms_patterns = [
    path('authentication', authentication, name = 'authentication'),
    path('quiz/<int:id_quiz>', quiz, name = 'quiz')
]

urlpatterns = [
    path('', include(webpages_patterns)),
    path('', include(forms_patterns))
]