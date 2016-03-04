from django.db import models
from datetime import datetime 

class Service(models.Model):
    title       = models.CharField(max_length=50)
    sub_tittle  = models.CharField(max_length=100)
    deatil      = models.TextField(max_length=500)
    icon        = models.ImageField(upload_to='flowlenders', blank=True)

    def __str__(self):
        return self.title


class New(models.Model):
    title       = models.CharField(max_length=50)
    sub_tittle  = models.CharField(max_length=100)
    deatil      = models.TextField(max_length=500)
    pdf_image   = models.ImageField(upload_to='flowlenders', blank=True)
    pdf_file    = models.ImageField(upload_to='flowlenders', blank=True)

    def __str__(self):
        return self.title

class Apply(models.Model):
    title       = models.CharField(max_length=50)
    sub_tittle  = models.CharField(max_length=100)
    deatil      = models.TextField(max_length=500)
    pdf_image   = models.ImageField(upload_to='flowlenders', blank=True)
    pdf_file    = models.ImageField(upload_to='flowlenders', blank=True)

    def __str__(self):
        return self.title

class Contect(models.Model):
    mailing_address = models.TextField(max_length=200)
    office_number   = models.CharField(max_length=50)
    toll_number     = models.CharField(max_length=50)
    fax_number      = models.CharField(max_length=50)
    email           = models.EmailField(max_length=254)

    def __str__(self):
        return self.mailing_address

class Feedback(models.Model):
    name       = models.TextField(max_length=50)
    phone      = models.CharField(max_length=50)
    email      = models.EmailField(max_length=50)
    message    = models.CharField(max_length=500)
    data_date  = models.DateTimeField(default=datetime.now, blank=True)


    def __str__(self):
        return self.name

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

    def save(self):
        self.debit_ratio = self.debit_for/self.ammount_request
        super(ClientDetail, self).save()



    def __str__(self):
        return self.business_name
