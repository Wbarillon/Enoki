from django.shortcuts import redirect, render

from enoki_app.views.controllers.authentication import authentication_controller
from enoki_app.views.controllers.home import home_controller
from enoki_app.views.controllers.quiz import quiz_controller
from enoki_app.views.controllers.quiz_list import quiz_list_controller


# Create your views here.

def home(request):
    template_name = 'webpages/home.html'

    if 'context' in request.session:
        context = request.session['context']
        del request.session['context']
    else:
        context = {

        }

    home_controller(request, context)

    return render(request, template_name, context)

def authentication(request):
    template_name = 'forms/authentication.html'

    if 'context' in request.session:
        context = request.session['context']
        del request.session['context']
    else:
        context = {

        }

    if authentication_controller(request, context) == 'home':
        return redirect('home')
    elif authentication_controller(request, context) == 'quiz_list':
        return redirect('quiz_list')
    else:
        return render(request, template_name, context)

def quiz_list(request):
    template_name = 'webpages/quiz_list.html'

    if 'context' in request.session:
        context = request.session['context']
        del request.session['context']
    else:
        context = {

        }

    quiz_list_controller(request, context)

    return render(request, template_name, context)

def quiz(request, id_quiz):
    template_name = 'forms/quiz.html'

    if 'context' in request.session:
        context = request.session['context']
        del request.session['context']
    else:
        context = {

        }

    quiz_controller(request, context, id_quiz)

    return render(request, template_name, context)