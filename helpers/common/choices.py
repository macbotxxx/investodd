from django.utils.translation import ugettext_lazy as _


class ModelChoices:

    A_DAY = '1'
    TWO_DAYS = '2'
    THREE_DAYS = '3'
    FOUR_DAYS = '4'
    FIVE_DAYS = '5'
    SIX_DAYS = '6'
    A_WEEK = '7'
    TWO_WEEKS = '14'
    THREE_WEEKS = '21'
    A_MONTH = '28'
    TWO_MONTHS = '56'
    THREE_MONTHS = '84'
    FOUR_MONTHS = '112'
    FIVE_MONTHS = '140'
    SIX_MONTHS = '168'
    SEVEN_MONTHS = '196'
    EIGHT_MONTHS = '224'
    NINE_MONTHS = '252'
    TEN_MONTHS = '280'
    ELEVEN_MONTHS = '308'
    A_YEAR = '336'


    PLAN_DURATION = (
        (A_DAY, _("A Day Plan")),
        (TWO_DAYS, _("Two Days Plan")),
        (THREE_DAYS, _("Three Days Plan")),
        (FOUR_DAYS, _("Four Days Plan")),
        (FIVE_DAYS, _("Five Days Plan")),
        (SIX_DAYS, _("Six Days Plan")),
        (A_WEEK, _("A Full Week Plan")),
        (TWO_WEEKS, _("Two Weeks Plan")),
        (THREE_WEEKS, _("Three Weeks Plan")),
        (A_MONTH, _("A Month Plan")),
        (TWO_MONTHS, _("Two Months Plan")),
        (THREE_MONTHS, _("Three Month Plan")),
        (FOUR_MONTHS, _("Four Months Plan")),
        (FIVE_MONTHS, _("Five Months Plan")),
        (SIX_MONTHS, _("Six Moonths Plan")),
        (SEVEN_MONTHS, _("Seven Months Plan")),
        (EIGHT_MONTHS, _("Eight Months Plan")),
        (NINE_MONTHS, _("Nine Months Plan")),
        (TEN_MONTHS, _("Ten Months Plan")),
        (ELEVEN_MONTHS, _("Eleven Months Plan")),
        (A_YEAR, _("A Year Plan")),
    )


    WALLET_PROVIDERS = (
        ("Bitcoin", _("Bitcoin")),
        ("Ethereum", _("Ethereum")),
        ("Litecoin", _("Litecoin")),
        ("Bitcoin Cash", _("Bitcoin Cash")),
        ("Binance Coin", _("Binance Coin")),
        ("USD Coin", _("USD Coin")),
        ("Tether", _("Tether")),
        ("TRON", _("TRON")),
    )

    DEPOSIT_STATUS = (
        ("pending", _("Pending")),
        ("verified", _("Verified")),
        ("rejected", _("Rejected")),
    )

    DEP_STATUS = (
        ("pending", _("Pending")),
        ("verified", _("Verified")),
        ("rejected", _("Rejected")),
    )