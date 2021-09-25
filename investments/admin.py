from django.contrib import admin
from .models import Investment_plan, Investment_History

@admin.register(Investment_plan)
class Investment_planAdmin(admin.ModelAdmin):
    list_display = ('plan_name', 'plan_percentage', 'minimum_amount', 'maximum_amount', 'plan_usage_per_user', 'plan_duration')
    list_display_links = ('plan_name', 'plan_percentage', 'minimum_amount', 'maximum_amount', 'plan_usage_per_user', 'plan_duration')


@admin.register(Investment_History)
class Investment_HistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'plan_name', 'amount_invested', 'crypto_amount_invested', 'investment_start_time', 'investment_end_time', 'status')
    list_display_links = ('user', 'plan_name', 'amount_invested', 'crypto_amount_invested', 'investment_start_time', 'investment_end_time', 'status')