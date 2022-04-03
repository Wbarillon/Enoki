from enoki_app.forms import (
    ActionForm,
    AuthenticationForm,
    InscriptionForm
)
from enoki_app.views.services.authentication import (
    user_inscription,
    user_login,
    user_logout
)


def authentication_controller(request, context):

    if request.method == 'POST':

        action_form = ActionForm(request.POST)

        if action_form.is_valid():

            action = action_form.cleaned_data.get('action')

            context.update({
                'state': action
            })

            if action == 'inscription':

                inscription_form = InscriptionForm()

                context.update({
                    'inscription_form': inscription_form
                })

            elif action == 'inscription_confirmation':

                inscription_form = InscriptionForm(request.POST)

                if user_inscription(request, inscription_form):

                    return 'quiz_list'

                else:

                    context.update({
                        'state': 'inscription',
                        'inscription_form': inscription_form
                    })

            elif action == 'login':

                login_form = AuthenticationForm()

                context.update({
                    'login_form': login_form
                })

            elif action == 'login_confirmation':

                login_form = AuthenticationForm(data = request.POST)

                if user_login(request, login_form):

                    return 'quiz_list'

                else:

                    context.update({
                        'state': 'login',
                        'login_form': login_form
                    })

            elif action == 'logout':

                if user_logout(request):

                    return 'home'