from tests.factories.account_factories import AccountFactory
from tests.factories.transaction_factories import TransactionFactory
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from faker import Faker

faker = Faker()


class AccountTestCases(APITestCase):

    def test_get_transaction_detail(self):

        account = AccountFactory().create_account()
        trasaction = TransactionFactory().create_transaction(account=account)

        url = reverse('transaction_detail', args=[trasaction.transaction_id])

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data['transaction_id'], trasaction.transaction_id)

    def test_delete_transaction_detail(self):
        account = AccountFactory().create_account()
        trasaction = TransactionFactory().create_transaction(account=account)

        url = reverse('transaction_detail', args=[trasaction.transaction_id])

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data['message'], 'Transaction Deleted')

    def test_create_transaction(self):

        account = AccountFactory().create_account()
        transaction = {
            'account_number': account.account_number,
            'amount': float(faker.random_number(digits=4)),
            'transaction_type': 'deposit'
        }
        url = reverse('transaction')

        response = self.client.post(url, transaction, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            response.data['amount'], transaction['amount'])
