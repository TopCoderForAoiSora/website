from django.contrib.auth.models import AnonymousUser
from django.test import Client, TestCase, RequestFactory
from django.urls import reverse
from .views import CreatePuzzleView
from .models import Puzzle


# Create your tests here.
class ViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.data = {'username': 'Tester', 'password': 'TesterPassword'}
        self.factory = RequestFactory()
        response = self.client.post(reverse('accounts:register'), self.data, follow=True)
        response.context[0]['user'].is_superuser = True

    def getPostRequest(self, url, data):
        request = self.factory.post(reverse(url), data, follow=True)
        request.user = AnonymousUser()
        request.session = self.client.session
        return request


class ListView(ViewTest):

    def test_no_puzzle_in_DB(self):
        response = self.client.get(reverse('puzzle:index'))

        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['all_puzzles_to_solve'], [])
        self.assertQuerysetEqual(response.context['all_solved_puzzles'], [])


class CreateView(ViewTest):

    def test_create_puzzle_success(self):
        data = {
            'location': '1',
            'title': 'TestPuzzle',
            'point': 10,
            'content': 'This is a test puzzle',
            'answer': 'No answer',
            'logo': 'www.google.com'
        }
        request = self.getPostRequest('puzzle:add_puzzle', data)
        response = CreatePuzzleView.as_view()(request)

        created_puzzle = Puzzle.objects.get(title='TestPuzzle')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/add/' + str(created_puzzle.pk) + '/')

    def test_create_puzzle_without_location(self):
        data = {
            'title': 'TestPuzzle',
            'point': 10,
            'content': 'This is a test puzzle',
            'answer': 'No answer',
            'logo': 'www.google.com'
        }
        request = self.getPostRequest('puzzle:add_puzzle', data)
        response = CreatePuzzleView.as_view()(request)

        created_puzzle = Puzzle.objects.all()
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(created_puzzle, [])
