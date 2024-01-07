from rest_framework import status
from rest_framework.test import APITestCase

from price.models import Price
from users.models import User


class PriceTestCase(APITestCase):
    """Price model testing"""

    def setUp(self) -> None:
        super().setUp()
        self.vendor = User.objects.create_user(
            first_name='TestName',
            last_name='TestLastName',
            username='vendor',
            password='1234',
            is_vendor=True,
            email='tester@test.com'
        )

    def test_create_price_unauthenticated(self):
        data = {
            'origin_price': "100",
        }

        response = self.client.post(
            path='/prices/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED
        )

    def test_create_price_authenticated(self):
        self.client.force_authenticate(user=self.vendor)

        data = {
            'origin_price': "100",
        }

        response = self.client.post(
            path='/prices/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.json(),
            {"origin_price": "100.000000",
             "full_price": 130.56,
             "tax": 0.06,
             "bank_commission": 0.02,
             "shop_commission": 0.2}
        )

        self.assertTrue(Price.objects.all().exists())
