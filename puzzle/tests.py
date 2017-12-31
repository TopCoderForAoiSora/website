from django.test import Client, TestCase
from django.urls import reverse


# Create your tests here.
class ViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.data = {'username': 'Tester', 'password': 'TesterPassword'}
        self.client.post(reverse('accounts:register'), self.data, follow=True)


class ListPuzzles(ViewTest):

    def test_no_puzzle_in_DB(self):
        response = self.client.get(reverse('puzzle:index'))

        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['all_puzzles_to_solve'], [])
        self.assertQuerysetEqual(response.context['all_solved_puzzles'], [])
