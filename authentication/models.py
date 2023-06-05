from django.db import models
from django.db.models.fields import CharField
from django.utils.translation import gettext_lazy as _
from .constants import PaymentStatus


class Order(models.Model):
    name = CharField(_("Customer Name"), max_length=254, blank=False, null=False)
    amount = models.FloatField(_("Amount"), null=False, blank=False)
    status = CharField(
        _("Payment Status"),
        default=PaymentStatus.PENDING,
        max_length=254,
        blank=False,
        null=False,
    )
    provider_order_id = models.CharField(
        _("Order ID"), max_length=40, null=False, blank=False
    )
    payment_id = models.CharField(
        _("Payment ID"), max_length=36, null=False, blank=False
    )
    signature_id = models.CharField(
        _("Signature ID"), max_length=128, null=False, blank=False
    )

    def __str__(self):
        return f"{self.id}-{self.name}-{self.status}"


class Temp(models.Model):
    name = models.CharField(max_length=20)
    otp = models.CharField(max_length=4,default=0)
    phone = models.CharField(max_length=20)
    max_otp_try = models.IntegerField(default=3)



class Signup(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    is_verified = models.BooleanField(default=False)

class Loan_registration(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    persontype = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    require_loan_amount = models.CharField(max_length=10)
    cibil_score = models.CharField(max_length=10)
    monthly_income = models.CharField(max_length=10)
    monthly_emi_you_pay = models.CharField(max_length=10)
    loan_purpose = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    emi_tenure = models.CharField(max_length=255)






