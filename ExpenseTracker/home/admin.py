from django.contrib import admin
from django.contrib.sessions.models import Session
from .models import Transactions
from .models import UserProfile

class TransactionsAdmin(admin.ModelAdmin):
    list_display = ("user", "transaction_type", "amount", "date", "category")

admin.site.register(Transactions, TransactionsAdmin)
admin.site.register(Session)
admin.site.register(UserProfile)
