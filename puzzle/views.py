from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView
from .forms import UserForm
from .models import Puzzle


class IndexView(generic.ListView):
    template_name = 'puzzle/index.html'
    context_object_name = 'all_puzzles'

    def get_queryset(self):
        return Puzzle.objects.all()


class DetailView(generic.DetailView):
    model = Puzzle
    template_name = 'puzzle/detail.html'


class CreatePuzzleView(CreateView):
    model = Puzzle
    fields = ['location', 'title', 'point', 'content', 'answer', 'logo']


def register(request):
    form = UserForm(request.POST or None)
    if not form.is_valid():
        context = {
            'form': form,
        }
        return render(request, 'puzzle/register.html', context)

    user = form.save(commit=False)
    username = form.cleaned_data['username']
    email = form.cleaned_data['email']
    password = form.cleaned_data['password']
    user.set_password(password)
    user.save()
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, 'puzzle/index.html')


def login_user(request):
    if request.method != "POST":
        return render(request, 'puzzle/login.html')

    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)

    if user is None:
        return render(request, 'puzzle/login.html', {'error_message': 'Invalid login'})

    login(request, user)
    return render(request, 'puzzle/index.html')


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'puzzle/login.html', context)