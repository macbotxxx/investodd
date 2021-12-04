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

import secrets


class Deposit (BaseModel):
    """ 
    User deposit history which include the status and payment gateways.
    """

    PAYMENTS_STATUS = (
        ('unverified', _('Unverified')),
        ('verified', _('Verified')),
        ('cancelled', _('Cancelled')),
        ('rejected', _('Rejected/Refused'))
    )

    user = models.ForeignKey(
        User,on_delete=models.PROTECT,
        verbose_name =_("User"),
        null=True,blank=True,
        help_text =_("The User associated with this deposit history")
    )

    transaction_type = models.CharField(
        verbose_name = _("Transaction Type"),
        max_length=200,
        default = "Deposited Funds",
        null=True,blank=True,
        help_text =_("Transaction Type of the current investors deposit ")
    )

    payment_gateway = models.CharField(
        verbose_name = _("Payment Gateway"),
        max_length= 200, null=True,
        blank=True,
        help_text =_("Payment Gateway of which the payment is been made through")
    )

    order_id = models.CharField(
        verbose_name = _("Transaction Order ID"),
        max_length= 200,
        null=True,blank=True,
        help_text=_("Transaction order ID of the investors transaction")
    )

    order = models.CharField(
        verbose_name = _("Order Type"),
        max_length=200,
        default = "Deposit",
        null=True,blank=True,
        help_text =_("Order Type of the current investors deposit ")
    )

    deposited_amount = models.FloatField(
        verbose_name = _("Deposit Amount"),
        default = 0,
        null=True,blank=True,
        help_text =_("Deposited Amount the investor current action")
    )

    crypto_deposit = models.FloatField(
        verbose_name = _("Deposit Amount In Crypto"),
        default = 0,
        null=True,blank=True,
        help_text =_("Deposited Amount the investor current action")
    )

    default_currency_id = models.CharField(
        max_length=3,
        verbose_name=_("Default Currency ID"),
        blank=True, null=True,
        default='USD',
        help_text=_("The default currency of the investor. Currency will be sent against investors country of residence.")
    )

    available_balance = models.FloatField(
        verbose_name=_("Available Balance"),
        null =True, blank=True, default = 0,
        help_text=_("The investors available balance for the account")
    )

    crypto_available_balance = models.FloatField(
        verbose_name=_("Crypto Balance"),
        null =True, blank=True, default = 0,
        help_text=_("The investors available balance in crypto currency , converting the available balance to crypto currency")
    )

    payment_status = models.CharField(
        choices=PAYMENTS_STATUS,
        default='unverified',
        max_length=50,
        null=True, blank=True,
        verbose_name=_("Payment Status"),
        help_text=_("The Payment status that holds the current state of the transaction")
    )

    reference_id = models.CharField(
        verbose_name=_("Payment Reference ID"),
        max_length=200, null=True,
        blank=True,
        help_text=_("Investors deposit Payment Reference ID, which is auto generated once the transaction is set to action")
    )

    transaction_details = models.CharField(
        verbose_name=_("Transaction Details"),
        max_length=200, null=True,
        blank=True,
        help_text=_("investors Transaction details , hold the customized note for the current transaction. eg. Deposit Fund for Investment or Deposit Fund for available balance.")
    )

    class Meta:
        ordering = ('-created_date',)
        verbose_name = _("All Deposited Fund")
        verbose_name_plural = _("All Deposited Fund")

    def save(self, *args, **kwargs) -> None:
        while not self.reference_id:
            reference_id = secrets.token_urlsafe(30).upper()
            order_id = secrets.token_hex(5).upper()
            
            object_with_similar_ref = Deposit.objects.filter(reference_id=reference_id, order_id=order_id)
            if not object_with_similar_ref:
                self.reference_id = reference_id
                self.order_id = order_id
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.user)















