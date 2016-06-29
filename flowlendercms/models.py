from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django import forms
from geoposition.fields import GeopositionField

class Promoter(models.Model):
      promoter_name = models.CharField(max_length=50)
      promoter_logo = models.ImageField(upload_to='documents')
      promoter_logo_large = models.ImageField(upload_to='documents')
      promoter_web = models.URLField(max_length=200)
      def __str__(self):
          return self.promoter_name

class EventDetail(models.Model):

        SUB = 'Submission Only'
        PON = 'Points'
        TIL = 'Time Limit'


        RULES = (
            (SUB, 'Submission Only'),
            (PON, 'Points'),
            (TIL, 'Time Limit'),
        )

        SE = 'Single Elimination'
        DE = 'Double Elimination'
        RR = 'Round Robin'

        BRACKET = (
            (SE, 'Single Elimination'),
            (DE, 'Double Elimination'),
            (RR, 'Round Robin'),
        )


        event_name = models.CharField( max_length=50)

        promoter = models.ForeignKey(
            'Promoter',
            on_delete=models.CASCADE,
        )
        date = models.DateField()
        location = models.CharField(max_length=50)
        address = models.CharField(max_length=50)
        city = models.CharField(max_length=50)
        state = models.CharField(max_length=50)
        zip_code = models.PositiveIntegerField(max_length=5)
        geo_code = GeopositionField()
        rule=models.CharField(max_length=25,
                            choices=RULES,
                            default=PON)
        bracket=models.CharField(max_length=25,
                            choices=BRACKET,
                            default=RR)
        gi=models.BooleanField(default=False)
        nogi=models.BooleanField(default=False)
        kids=models.BooleanField(default=False)
        pro=models.BooleanField(default=False)
        purse=models.BooleanField(default=False)
        absolute=models.BooleanField(default=False)
        adults=models.BooleanField(default=False)
        kids_special_format=models.BooleanField(default=False)
        kids_special_rules=models.CharField(max_length=25,
                            choices=RULES,
                            default=PON)
        kids_special_format=models.CharField(max_length=25,
                            choices=BRACKET,
                            default=RR)
        cost=models.PositiveIntegerField(max_length=5)
        predate=models.DateField()
        cost_late=models.PositiveIntegerField(max_length=5)
        cutoff_date=models.DateField()
        event_description=models.TextField(max_length=200)
        small_image=models.ImageField(upload_to='documents')
        large_image=models.ImageField(upload_to='documents')

        added = models.DateTimeField(auto_now_add=True)
        updated = models.DateTimeField(auto_now=True)
