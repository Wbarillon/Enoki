from django.shortcuts import redirect, render

from enoki_app.views.controllers.authentication import authentication_controller
from enoki_app.views.controllers.home import home_controller


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
    elif authentication_controller(request, context) == 'etat_jardin':
        return redirect('etat_jardin')
    else:
        return render(request, template_name, context)