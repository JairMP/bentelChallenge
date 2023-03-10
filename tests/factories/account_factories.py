from faker import Faker

from bank.models import Account

faker = Faker()


class AccountFactory:

    def build_account_json(self):
        return {
            'account_number': str(faker.random_number(digits=8)),
            'balance': float(faker.random_number(digits=4)),
            'customer_name': faker.name(),
            'account_type': 'checking'
        }

    def create_account(self):
        return Account.objects.create(**self.build_account_json())
