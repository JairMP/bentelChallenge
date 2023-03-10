from django.urls import path
from .api import account_api_view, transaction_api_view, account_detail_api_view, transaction_detail_api_view, transactions_account_api_view

urlpatterns = [
    path('account/', account_api_view, name='account'),
    path('account/<str:account_number>/',
         account_detail_api_view, name='account_detail'),
    path('transaction/', transaction_api_view, name='transaction'),
    path('transaction/<str:transaction_id>/',
         transaction_detail_api_view, name='transaction_detail'),
    path('transaction/account/<str:account_number>/',
         transactions_account_api_view, name='transaction_account_detail')
]
