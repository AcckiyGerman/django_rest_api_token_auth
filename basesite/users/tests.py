from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


username = 'testuser'
password = 'testpass'


# Create your tests here.
class UsersAuthTests(APITestCase):
    def test_application_is_working(self):
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, 200)

    def test_register(self):
        response = self.client.post(
            '/users/register/',
            {'username': username, 'password': password},
            format='json'
        )
        self.assertEqual(response.data['status'], 'success')
        self.assertTrue(response.data.get['token'])
        self.assertTrue(User.objects.get_by_natural_key(username=username))

    def login(self):
        response = self.client.post(
            '/users/register/',
            {'username': username, 'password': password},
            format='json'
        )

        user = User.objects.get_by_natural_key(username=username)
        self.assertEqual(response.data['token'], user.token.key)

    def test_protected_returns_proper_error_for_non_auth_users(self):
        response = self.client.get('/users/protected/')
        self.assertEqual(response.status_code, 401)
        self.assertTrue(response.data['error'])

    def test_protected_for_auth_users(self):
        # Include an appropriate `Authorization:` header on all requests.
        token = Token.objects.get(user__username=username)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.get('/users/protected/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.data['message'])
