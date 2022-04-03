from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from enoki_app.models import (
    AnswerChoice,
    CustomUser,
    Question
)


class ActionForm(forms.Form):

    django_object_id = forms.IntegerField(required = False)
    action = forms.CharField()

class InscriptionForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ['nickname', 'email', 'password1', 'password2']

class QuizForm(forms.Form):

    def __init__(self, *args, **kwargs):

        quiz = kwargs.pop('quiz')

        super(QuizForm, self).__init__(*args, **kwargs)

        for i in range(len(quiz)):            

            self.fields['question_'+str(i + 1)] = forms.CharField(
                label = quiz[i]['question'],
                widget = forms.CheckboxSelectMultiple(
                    choices = [list(stuff.items())[0] for stuff in quiz[i]['answers_choice']]
                )
            )