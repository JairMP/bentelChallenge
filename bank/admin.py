from django.contrib import admin
from .models import Account, Transaction


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    pass


@admin.register(Transaction)
class AccountAdmin(admin.ModelAdmin):
    pass
