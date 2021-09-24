from helpers.common.basemodel import BaseModel
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.urls import reverse

import uuid



class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError(_('The given email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self._create_user(email, password, **extra_fields)

class User(AbstractUser):
    """Default user for investodd."""
    objects = UserManager()

    KYC_STATUS = (
        ('unverified', _('Unverified')),
        ('pending', _('Pending')),
        ('verified', _('Verified')),
        ('action_required', _('Action_required')),
        ('cancelled', _('Cancelled')),
        ('rejected', _('Rejected/Refused'))
    )


    id = models.UUIDField(
        default = uuid.uuid4,
        editable=False,
        primary_key=True,
        help_text=_("The unique identifier of the investor.")
    )


    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)

    email = models.EmailField(
        max_length=150,
        null=True,
        unique=True,
        verbose_name=_("Email Address"),
        help_text=_("The email address of the investor.")
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    username = None


    first_name = models.CharField(
        verbose_name=_("First names"),
        max_length=50,
        null=True,
        help_text=_("The first nammes of the investor.")
    )

    last_name = models.CharField(
        max_length=50,
        verbose_name=_("Last names"),
        null=True,
        help_text=_("The last nammes of the investor.")
    )

    date_of_birth = models.DateField(
        verbose_name=_("Date of birth"),
        blank=True,
        null=True,
        help_text=_("The date of birth of the customer.")
    )

    kyc_complete = models.BooleanField(
        verbose_name=_("KYC complete"),
        default=False,
        help_text=_("Flag to determine if a cutomer have completed KYC verification")
    )

    kyc_complete_date = models.DateTimeField(
        verbose_name=_("KYC complete date"),
        blank=True,
        null=True,
        help_text=_("Timestamp when customer completed KYC verifiction process.")
    )

    kyc_status = models.CharField(
        max_length=15,
        verbose_name=_("KYC status"),
        choices=KYC_STATUS,
        default='Unverified',
        blank=True,
        null=True,
        help_text=_("The .")
    )


    kyc_submitted = models.BooleanField(
        verbose_name=_("KYC submitted"),
        blank=True,null=True,
        help_text=_("Flag to determine if customer has submitted a KYC verification.")
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

    withdrawal_balance = models.FloatField(
        verbose_name=_("Withdrawal Balance"),
        null =True, blank=True, default = 0,
        help_text=_("The investors withdrable balance for the account")
    )

    crypto_withdrawal_balance = models.FloatField(
        verbose_name=_("Crypto Withdrawal Balance"),
        null =True, blank=True, default = 0,
        help_text=_("The investors withdrable balance in crypto converting the withdrawable balance to crypto currency")
    )

    referral_bonus = models.FloatField(
        verbose_name=_("Referral Bonus"),
        null =True, blank=True, default = 0,
        help_text=_("The investors referral bonus balance for the account")
    )

    crypto_referral_bonus = models.FloatField(
        verbose_name=_("Crypto Referral Balance"),
        null =True, blank=True, default = 0,
        help_text=_("The investors withdrable balance in crypto converting the referral balance to crypto currency")
    )

   

    class Meta:
        verbose_name = _("Register Investor")
        verbose_name_plural = _("Register Investor")

    def __str__(self):
        return str(self.email)


    def get_absolute_url(self):
        """
        Get url for user's detail view.
        Returns:
            str: URL for user detail.
        """
        return reverse("users:detail", kwargs={"username": self.pk})



class UserActivity (BaseModel):
    """ 
    An Activity Log (also known as an Activity Diary ) is a written record of how a user spend time. 
     you can then change the way that you work to eliminate them.
    """

    user = models.ForeignKey(
        'User',
        verbose_name=_("User Profile"),
        on_delete=models.PROTECT,
        help_text=_("The user for whom account belongs to")
    )

    hostname = models.CharField(
        verbose_name=_("Host Name"),
        max_length=355,
        null=True,blank=True,
        help_text=_("The Host Name of the logged in user system")
    )

    ip_address = models.GenericIPAddressField(
        verbose_name=_("System IP Address"),
        null=True, blank=True, 
        editable=False,
        help_text=_(" The system IP address to current login user")
    )

    class Meta:
        verbose_name = _("User Activity")
        verbose_name_plural = _("User Activity")

    def __str__(self):
        return self.user


    

    
