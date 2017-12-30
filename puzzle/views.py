from django.shortcuts import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.core.urlresolvers import reverse_lazy
from .models import Puzzle, PlayerGameHistory


class IndexView(ListView):
    template_name = 'puzzle/index.html'
    context_object_name = 'all_puzzles_to_solve'

    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(*args, **kwargs)

        player_game_history = PlayerGameHistory.objects.get(user=self.request.user)
        all_solved_puzzles = player_game_history.solved.all()

        context['all_solved_puzzles'] = all_solved_puzzles

        player_curr_score = 0
        for puzzle in all_solved_puzzles:
            player_curr_score += puzzle.point
        context['player_score'] = player_curr_score

        player_game_history.score = player_curr_score
        player_game_history.save()

        return context

    def get_queryset(self):
        return PlayerGameHistory.objects.get(user=self.request.user).toSolve.all()


class PuzzleDetailView(DetailView):
    model = Puzzle
    template_name = 'puzzle/detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DetailView, self).get_context_data(*args, **kwargs)
        puzzle = self.get_object()

        context['is_solved'] = False
        if puzzle in PlayerGameHistory.objects.get(user=self.request.user).solved.all():
            context['is_solved'] = True

        return context


class CreatePuzzleView(CreateView):
    model = Puzzle
    fields = ['location', 'title', 'point', 'content', 'answer', 'logo']

    def get_success_url(self):
        return reverse('puzzle:add_new_puzzle_to_all_player', args=(self.object.id,))


class UpdatePuzzleView(UpdateView):
    model = Puzzle
    fields = ['location', 'title', 'point', 'content', 'answer', 'logo']


class DeletePuzzleView(DeleteView):
    model = Puzzle
    success_url = reverse_lazy('puzzle:index')


def init_user_game_history(request):
    player_game_history = PlayerGameHistory(user=request.user, score=0, solved=(), toSolve=Puzzle.objects.all())
    player_game_history.save()

    return HttpResponseRedirect('/')


def add_new_puzzle_to_all_player(request, puzzle_id):
    new_puzzle = Puzzle.objects.get(pk=puzzle_id)
    for player_game_history in PlayerGameHistory.objects.all():
        player_game_history.toSolve.add(new_puzzle)

    return HttpResponseRedirect('/')


def update_user_game_history(request, puzzle_id):
    player_game_history = PlayerGameHistory.objects.get(user=request.user)
    solved_puzzle = Puzzle.objects.get(id=puzzle_id)

    player_game_history.solved.add(solved_puzzle)
    player_game_history.toSolve.remove(solved_puzzle)

    player_game_history.save()
    return HttpResponseRedirect('/')

