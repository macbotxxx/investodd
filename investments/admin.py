from django.contrib import admin
from .models import Investment_plan

@admin.register(Investment_plan)
class Investment_planAdmin(admin.ModelAdmin):
    list_display = ('plan_name', 'plan_percentage', 'minimum_amount', 'maximum_amount', 'plan_usage_per_user', 'plan_duration')
    list_display_links = ('plan_name', 'plan_percentage', 'minimum_amount', 'maximum_amount', 'plan_usage_per_user', 'plan_duration')
