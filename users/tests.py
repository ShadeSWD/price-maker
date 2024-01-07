from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class UserTestCase(APITestCase):
    """Price model testing"""

    def setUp(self) -> None:
        self.admin = User.objects.create_superuser(username='admin', password='admin')

    def test_create_user_unauthenticated(self):
        data = {
            "first_name": 'TestName',
            "last_name": 'TestLastName',
            "username": 'vendor',
            "password": '1234',
            "is_vendor": "True",
            "email": 'tester@test.com'
        }

        response = self.client.post(
            path='/users/prices/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED
        )

    def test_create_user_authenticated(self):
        self.client.force_authenticate(user=self.admin)

        data = {
            "first_name": 'TestName',
            "last_name": 'TestLastName',
            "username": 'vendor',
            "password": '1234',
            "is_vendor": "True",
            "email": 'tester@test.com'
        }

        response = self.client.post(
            path='/users/prices/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertTrue(User.objects.all().exists())
