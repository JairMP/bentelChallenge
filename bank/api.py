from .models import Account, Transaction
from rest_framework.decorators import api_view
from .serializers import AccountSerializer, TransactionSerializer, AccountUpdateSerializer, TransactionUpdateSerializer
from rest_framework.response import Response
import shortuuid
from rest_framework import status

################# ACCOUNT #################


@api_view(['GET', 'POST'])
def account_api_view(request):

    if request.method == 'GET':
        accounts = Account.objects.all()
        accounts_serializer = AccountSerializer(accounts, many=True)
        return Response(accounts_serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        data = request.data
        data['account_number'] = shortuuid.uuid()
        account_serializer = AccountSerializer(data=request.data)

        if account_serializer.is_valid():
            account_serializer.save()
            return Response(account_serializer.data, status=status.HTTP_201_CREATED)

        return Response(account_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


################# ACCOUNT WITH ID #################

@api_view(['GET', 'PUT', 'DELETE'])
def account_detail_api_view(request, account_number=None):
    account = Account.objects.filter(
        account_number=account_number).first()

    if account:

        if request.method == 'GET':
            if account_number:
                account_serializer = AccountSerializer(account)
                return Response(account_serializer.data, status=status.HTTP_200_OK)

        elif request.method == 'PUT':
            data = request.data

            account_serializer = AccountUpdateSerializer(
                account, data=request.data)

            if account_serializer.is_valid():
                account_serializer.save()
                return Response(account_serializer.data, status=status.HTTP_200_OK)

            return Response(account_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            account.delete()
            return Response({'message': 'Account Deleted'}, status=status.HTTP_200_OK)

    return Response({'message': 'Account Not Found'}, status=status.HTTP_404_NOT_FOUND)


################# TRANSACTIONS #################

@api_view(['GET', 'POST'])
def transaction_api_view(request):
    if request.method == 'GET':
        transactions = Transaction.objects.all()

        transactions_serializer = TransactionSerializer(
            transactions, many=True)
        return Response(transactions_serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        data = request.data

        if not data.get('amount') or float(data.get('amount')) <= 0:
            return Response({'message': 'Amount cant be 0 or negative value'}, status=status.HTTP_400_BAD_REQUEST)

        account = Account.objects.filter(
            account_number=data["account_number"]).first()

        if not account:
            return Response({'message': 'Account Not Found'}, status=status.HTTP_404_NOT_FOUND)

        data['transaction_id'] = shortuuid.uuid()

        transaction_serializer = TransactionSerializer(
            data=data, context={'account_number': account})

        if transaction_serializer.is_valid():

            if data.get('transaction_type') == "deposit":

                account.balance += data['amount']
                account.save()

            elif data.get('transaction_type') == "withdrawal":

                if account.balance == 0:
                    return Response({'message': 'Balance is 0'}, status=status.HTTP_400_BAD_REQUEST)

                account.balance -= data['amount']
                account.save()

            transaction_serializer.save()
            return Response(transaction_serializer.data, status=status.HTTP_201_CREATED)

        return Response(transaction_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


################# TRANSACTIONS WITH ID #################

@api_view(['GET', 'PUT', 'DELETE'])
def transaction_detail_api_view(request, transaction_id=None):
    transaction = Transaction.objects.filter(
        transaction_id=transaction_id).first()

    if transaction:
        if request.method == 'GET':
            if transaction_id:
                transaction_serializer = TransactionSerializer(transaction)
                return Response(transaction_serializer.data, status=status.HTTP_200_OK)

        elif request.method == 'PUT':
            transaction_serializer = TransactionUpdateSerializer(
                transaction, data=request.data)
            if transaction_serializer.is_valid():
                transaction_serializer.save()
                return Response(transaction_serializer.data, status=status.HTTP_200_OK)

            return Response(transaction_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            transaction.delete()
            return Response({'message': 'Transaction Deleted'}, status=status.HTTP_200_OK)

    return Response({'message': 'Transaction Not Found'}, status=status.HTTP_404_NOT_FOUND)


################# TRANSACTIONS ASSOCIATED TO ACCOUNT ##################

@api_view(['GET'])
def transactions_account_api_view(request, account_number=None):

    if request.method == 'GET':
        transactions = Transaction.objects.filter(
            account_number=account_number)

        transactions_serializer = TransactionSerializer(
            transactions, many=True)

        return Response(transactions_serializer.data, status=status.HTTP_200_OK)

    return Response({'message': 'Account Not Found'}, status=status.HTTP_404_NOT_FOUND)
