from django.views import generic
from django.views.generic.edit import CreateView
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