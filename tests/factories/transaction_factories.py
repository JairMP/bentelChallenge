from faker import Faker

from bank.models import Transaction

faker = Faker()


class TransactionFactory:

    def build_transaction_json(self, account):
        return {
            'transaction_id': str(faker.random_number(digits=8)),
            'account_number': account,
            'amount': float(faker.random_number(digits=4)),
            'transaction_type': 'deposit'
        }

    def create_transaction(self, account):
        return Transaction.objects.create(**self.build_transaction_json(account))
