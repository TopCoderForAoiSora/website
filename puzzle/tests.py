from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse
from .models import Puzzle, PlayerGameHistory

# Create your tests here.
class ListPuzzles(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('Tester', 'Tester@gmail.com', 'TesterPassword')
        player_game_history = PlayerGameHistory(user=self.user, score=0, solved=(), toSolve=Puzzle.objects.all())
        player_game_history.save()
        self.client.login(username='Tester', password='TesterPassword')
    
    def test_no_puzzle_in_DB(self):
        response = self.client.get(reverse('puzzle:index'))
        
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['all_puzzles_to_solve'], [])
        self.assertQuerysetEqual(response.context['all_solved_puzzles'], [])
        