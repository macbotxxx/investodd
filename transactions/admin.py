from django.contrib import admin
from .models import Deposit

# Register your models here.

@admin.register(Deposit)
class DepositAdmin(admin.ModelAdmin):
    list_display = ('user', 'transaction_type', 'payment_gateway', 'order_id')
    list_display_links = ('user', 'transaction_type', 'payment_gateway', 'order_id')
