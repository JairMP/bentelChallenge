from django.db import models


class Account(models.Model):

    ACCOUNT_TYPES = (("savings", "savings"), ("checking", "checking"))

    account_number = models.CharField(
        unique=True, max_length=50)
    balance = models.FloatField()
    customer_name = models.CharField(max_length=50)
    account_type = models.CharField(max_length=50, choices=ACCOUNT_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Transaction(models.Model):

    TRANSACTION_TYPES = (("deposit", "deposit"), ("withdrawal", "withdrawal"))

    transaction_id = models.CharField(
        unique=True, max_length=50)
    account_number = models.ForeignKey(
        Account, to_field='account_number', on_delete=models.CASCADE)
    amount = models.FloatField()
    transaction_type = models.CharField(
        max_length=50, choices=TRANSACTION_TYPES)
    transaction_description = models.CharField(max_length=50, null=True)
    status = models.CharField(max_length=10, default="success")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
