from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from enoki_app.models import (
    CustomUser
)


class ActionForm(forms.Form):

    django_object_id = forms.IntegerField(required = False)
    action = forms.CharField()

class InscriptionForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ['nickname', 'email', 'password1', 'password2']