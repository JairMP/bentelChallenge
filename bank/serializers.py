from rest_framework import serializers
from .models import Account, Transaction


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('__all__')


class AccountUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('__all__')
        read_only_fields = ('account_number', 'balance', 'created_at')


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('__all__')
