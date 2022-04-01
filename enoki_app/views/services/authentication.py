from django.contrib.auth import login, authenticate, logout

def user_inscription(request, inscription_form):
    if inscription_form.is_valid():
        inscription_form.save()
        nickname = inscription_form.cleaned_data.get('nickname')
        email = inscription_form.cleaned_data.get('email')
        password = inscription_form.cleaned_data.get('password1')
        account = authenticate(nickname = nickname, email = email, password = password)
        login(request, account)

        return True

def user_login(request, login_form):
    if login_form.is_valid():
        nickname = login_form.cleaned_data.get('username')
        password = login_form.cleaned_data.get('password')
        user = authenticate(nickname = nickname, password = password)
        if user is not None:
            login(request, user)
            
            return True

def user_logout(request):
    logout(request)

    return True