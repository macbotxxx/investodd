from django.core.exceptions import ValidationError
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils import timezone

from datetime import date, datetime
from django.utils.translation import gettext_lazy as _
from django.db import models
import uuid
import datetime

from investodd.users.models import User
from helpers.common.basemodel import BaseModel
from helpers.common.choices import ModelChoices




class Investment_plan (BaseModel):
    """ Investment Plan Model Data """

    plan_name = models.CharField(
        verbose_name=_("Investment Plan Name"),
        null=True, blank=True,
        max_length=200,
        help_text=_("The investment name given to the plan available to be invested on")
    )

    plan_percentage = models.PositiveIntegerField(
        verbose_name=_("Investment Plan Percentage"),
        null=True, blank=True,
        help_text=_("Investment plan percentage given to take action when the plan is activated.")
    )

    minimum_amount = models.FloatField(
        verbose_name=_("Plan Minimum Amount"),
        default=0,
        null=True, blank=True,
        max_length=200,
        help_text=_("Investment plan minimum amount for the plan.")
    )

    maximum_amount = models.FloatField(
        verbose_name=_("Investment Plan Maximum Amount"),
        null=True, blank=True,
        default=0,
        max_length=200,
        help_text=_("Investment plan maximum amount for the plan.")
    )

    plan_usage_per_user = models.PositiveIntegerField(
        verbose_name=_("Investment Plan Usage Per User"),
        null=True, blank=True,
        help_text=_("Investment plan Usage was introduced to help and restrict users from reinvesting on the same investment plan, which after exceeding a particular duration the investor is instructed to invest on a new plan.")
    )    

    plan_duration = models.CharField(
        choices=ModelChoices.PLAN_DURATION,
        verbose_name=_("Investment Plan Percentage"),
        null=True, blank=True,
        max_length=200,
        help_text=_("Investment plan percentage given to take action when the plan is activated, NOTE-- the investment plan is meant to terminate after the duration which both the interest and capital will be added to the investor, INTEREST IS BEEN ADDED AFTER THE DURATION NOT HOURLY.")
    )

     #Metadata
    class Meta :
        verbose_name = _("Setup Investment Plan")
        verbose_name_plural = _("Setup Investment Plan")
        

    def __str__(self):
        return str(self.plan_name)


    def clean_fields(self, exclude=None):
        super().clean_fields(exclude=exclude)
        if self.minimum_amount == self.maximum_amount:
            raise ValidationError(
                {
                    'minimum_amount': _(
                        "The minimum amount cant be the same with the maximum amount."
                    ),
                }
            )
        if self.minimum_amount > self.maximum_amount:
            raise ValidationError(
                {
                    'minimum_amount': _(
                        "The minimum amount cant be higher than the maximum amount."
                    ),
                }
            )
        
        