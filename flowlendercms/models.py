from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django import forms

class Profile(models.Model):
    user = models.OneToOneField(User)
    timein = models.TimeField()
    timeout = models.TimeField()
    bio = models.TextField()
    image = models.ImageField()

class ClientDetail(models.Model):

    SBT = 'Submitted'
    FUN = 'Funded'
    DEC = 'Declined'
    WFD = 'Waiting for Further Documents'

    CURRENT_STATUS = (
        (SBT, 'Submitted'),
        (FUN, 'Funded'),
        (DEC, 'Declined'),
        (WFD, 'Waiting for Further Documents'),
    )

    WK = 'Weekly'
    BW = 'Bi-Weekly'
    MT = 'Monthly'

    PAYMENT_PLAN = (
        (WK, 'Weekly'),
        (BW, 'Bi-Weekly'),
        (MT, 'Monthly'),
    )

    business_name   = models.CharField(max_length=50)
    reffering_party = models.CharField(max_length=50)
    data_date = models.DateTimeField(default=datetime.now, blank=True)
    ammount_request = models.DecimalField(max_digits=5, decimal_places=2)
    debit_for = models.DecimalField(max_digits=5, decimal_places=2)
    payment_plan    = models.CharField(max_length=16,
                                        choices=PAYMENT_PLAN,
                                        default=WK)
    credit_score    = models.DecimalField(max_digits=5, decimal_places=2)
    current_status  = models.CharField(max_length=16,
                                        choices=CURRENT_STATUS,
                                        default=SBT)
    contact_name    = models.CharField(max_length=50)
    mailing_address = models.TextField(max_length=200,default="NIL")
    office_number   = models.CharField(max_length=50,default="NIL")
    mobile_number   = models.CharField(max_length=50,default="NIL")
    fax_number      = models.CharField(max_length=50,default="NIL")
    email           = models.EmailField(max_length=254,default="def@def.def")
    debit_ratio     = models.DecimalField(max_digits=5, decimal_places=2)


    def __str__(self):
        return self.business_name
