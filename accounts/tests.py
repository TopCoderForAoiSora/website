from django.test import Client, TestCase
from django.urls import reverse


# Create your tests here.
class AccountTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.data = {'username': 'Tester', 'password': 'TesterPassword'}
        self.client.post(reverse('accounts:register'), self.data, follow=True)
        # User will automatically login after register. Therefore, logout first.
        self.client.get(reverse('accounts:logout'), follow=True)


class AccountLoginTest(AccountTest):

    def test_login_succeed(self):
        response = self.client.post(reverse('accounts:login'), self.data, follow=True)

        self.assertTrue(response.context[0]['user'].is_authenticated())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.redirect_chain, [('/', 302)])

    def test_login_wrongGetRequest(self):
        response = self.client.get(reverse('accounts:login'), self.data, follow=True)

        self.assertFalse(response.context[0]['user'].is_authenticated())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.redirect_chain, [])

    def test_login_userNoExist(self):
        data = {'username': 'FakeTester', 'password': 'TesterPassword'}
        response = self.client.post(reverse('accounts:login'), data, follow=True)

        self.assertFalse(response.context[0]['user'].is_authenticated())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.redirect_chain, [])
        self.assertEqual(response.context[0]['error_message'], 'Invalid login')


class AccountLogoutTest(AccountTest):

    def setUp(self):
        self.client.login(username='Tester', password='TesterPassword')

    def test_logout_succeed(self):
        response = self.client.get(reverse('accounts:logout'), follow=True)

        self.assertFalse(response.context[0]['user'].is_authenticated())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.redirect_chain, [('/accounts/login/', 302)])


class AccountRegisterTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_register_succeed(self):
        data = {'username': 'Tester', 'password': 'TesterPassword'}
        response = self.client.post(reverse('accounts:register'), data, follow=True)

        self.assertTrue(response.context[0]['user'].is_authenticated())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.redirect_chain, [('/initUserGameHistory/', 302), ('/', 302)])

    def test_register_noUsername(self):
        data = {'password': 'TesterPassword'}
        response = self.client.post(reverse('accounts:register'), data, follow=True)

        self.assertFalse(response.context[0]['user'].is_authenticated())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.redirect_chain, [])

# class AccountActionTest(TestCase):
#
#     def setUp(self):
#         self.client = Client()
#         self.factory = RequestFactory()
#
#     def getGetRequest(self, url, data):
#         request = self.factory.get(reverse(url), data)
#         request.user = AnonymousUser()
#         request.session = self.client.session
#         return request
#
#     def getPostRequest(self, url, data):
#         request = self.factory.post(reverse(url), data)
#         request.user = AnonymousUser()
#         request.session = self.client.session
#         return request
#
#     def test_login_success(self):
#         data = {'username': 'Tester', 'password': 'TesterPassword'}
#         response = self.client.post(reverse('accounts:login'), data, follow=True)
#
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.redirect_chain, [('/', 302)])

#     def test_login_succeed(self):
#         data = {'username': 'Tester', 'password': 'TesterPassword'}
#         request = self.getPostRequest('accounts:login', data)
#         response = views.login_user(request)
#
#         self.assertTrue(request.user.is_authenticated())
#         self.assertEqual(response.status_code, 302)
#         self.assertEqual(response.url, '/')
#
#     def test_login_wrongGetRequest(self):
#         data = {'username': 'Tester', 'password': 'TesterPassword'}
#         request = self.getGetRequest('accounts:login', data)
#         response = views.login_user(request)
#
#         self.assertFalse(request.user.is_authenticated())
#         self.assertEqual(response.status_code, 200)
#
#     def test_login_userNoExist(self):
#         data = {'username': 'FakeTester', 'password': 'TesterPassword'}
#         request = self.getPostRequest('accounts:login', data)
#         response = views.login_user(request)
#
#         print(response.context_data)
#         self.assertFalse(request.user.is_authenticated())
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.context[0]['error_message'], 'Invalid login')
