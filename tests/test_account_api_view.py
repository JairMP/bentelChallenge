from tests.factories.account_factories import AccountFactory
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from faker import Faker

faker = Faker()


class AccountTestCases(APITestCase):

    def test_get_account_detail(self):
        account = AccountFactory().create_account()

        url = reverse('account_detail', args=[account.account_number])

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data['account_number'], account.account_number)

    def test_delete_account_detail(self):
        account = AccountFactory().create_account()

        url = reverse('account_detail', args=[account.account_number])

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data['message'], 'Account Deleted')

    def test_create_account(self):

        account = {
            'balance': float(faker.random_number(digits=4)),
            'customer_name': faker.name(),
            'account_type': 'checking'
        }
        url = reverse('account')

        response = self.client.post(url, account, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            response.data['balance'], account['balance'])
        self.assertEqual(
            response.data['customer_name'], account['customer_name'])
