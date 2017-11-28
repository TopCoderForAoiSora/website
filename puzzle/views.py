from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .forms import UserForm
from .models import Puzzle


class IndexView(ListView):
    template_name = 'puzzle/index.html'
    context_object_name = 'all_puzzles'

    def get_queryset(self):
        return Puzzle.objects.all()


class DetailView(DetailView):
    model = Puzzle
    template_name = 'puzzle/detail.html'


class CreatePuzzleView(CreateView):
    model = Puzzle
    fields = ['location', 'title', 'point', 'content', 'answer', 'logo']


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
                return HttpResponseRedirect('/')

    context = {
        'form': form,
    }
    return render(request, 'puzzle/register.html', context)


def login_user(request):
    if request.method != "POST":
        return render(request, 'puzzle/login.html')

    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)

    if user is None:
        return render(request, 'puzzle/login.html', {'error_message': 'Invalid login'})

    login(request, user)
    return HttpResponseRedirect('/')


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')

