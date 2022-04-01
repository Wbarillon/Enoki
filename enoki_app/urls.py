from django.urls import include, path

from enoki_app.views.index import (
    authentication,
    home
)

webpages_patterns = [
    path('', home, name = 'home')
]

forms_patterns = [
    path('authentication', authentication, name = 'authentication')
]

urlpatterns = [
    path('', include(webpages_patterns)),
    path('', include(forms_patterns))
]