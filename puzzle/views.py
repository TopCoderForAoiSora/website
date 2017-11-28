from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView
from .forms import UserForm
from .models import Puzzle


def index(request):
    if not request.user.is_authenticated():
        return render(request, 'puzzle/login.html')

    all_puzzles = Puzzle.objects.all()
    return render(request, 'puzzle/index.html', {'all_puzzles': all_puzzles})


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
                all_puzzles = Puzzle.objects.all()
                return render(request, 'puzzle/index.html', {'all_puzzles': all_puzzles})

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
    all_puzzles = Puzzle.objects.all()
    return render(request, 'puzzle/index.html', {'all_puzzles': all_puzzles})


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'puzzle/login.html', context)
