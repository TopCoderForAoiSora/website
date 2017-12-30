from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, HttpResponseRedirect
from .forms import UserForm


# Create your views here.
def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/initUserGameHistory/')

    context = {'form': form}
    return render(request, 'accounts/register.html', context)


def login_user(request):

    if request.method != "POST":
        return render(request, 'accounts/login.html')

    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)

    if user is None:
        return render(request, 'accounts/login.html', {'error_message': 'Invalid login'})

    login(request, user)
    return HttpResponseRedirect('/')


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')

