from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django import forms
from geoposition.fields import GeopositionField
from django.utils.safestring import mark_safe

class Promoter(models.Model):
      promoter_name = models.CharField(max_length=50, verbose_name='Promoter Name')
      promoter_logo = models.ImageField(upload_to='documents', default = 'documents/no-img.jpeg', verbose_name='Promoter Logo')
      promoter_logo_large = models.ImageField(upload_to='documents', default = 'documents/no-img.jpeg', verbose_name='Promoter Logo(Large)')
      promoter_web = models.URLField(max_length=200, blank=True, verbose_name='Promoter Website')
      def __str__(self):
          return self.promoter_name
      def image_tag(self):
          return mark_safe('<img src="%s" width="150" height="150" />' % (self.promoter_logo.url))

      image_tag.short_description = 'Image'

      class Meta:
        verbose_name_plural = "Promoter Details"


class EventDetail(models.Model):

        PON = 'Points'
        SUB = 'Submission Only'
        TIL = 'Time Limit'


        RULES = (
            (PON, 'Points'),
            (SUB, 'Submission Only'),
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


        event_name = models.CharField( max_length=50, verbose_name='Event Name')

        event_promoter = models.ForeignKey(
            'Promoter',
            on_delete=models.CASCADE, verbose_name='Promoter Name'
        )
        event_date = models.DateField(verbose_name='Event Date')
        event_geocode = GeopositionField(verbose_name='GEO Code')
        event_tentitive=models.BooleanField(default=False,verbose_name='Is Tentative?')

        end_date = models.DateField(verbose_name='Event End Date', blank=True, null=True)
        location = models.CharField(max_length=200,blank=True,null=True,verbose_name='Event Location')
        address = models.CharField(max_length=300,blank=True,null=True,verbose_name='Address')
        city = models.CharField(max_length=50,blank=True, null=True)
        state = models.CharField(max_length=50,blank=True, null=True)
        zip_code = models.PositiveIntegerField(max_length=5,blank=True, null=True, verbose_name='Zip Code')

        rule=models.CharField(max_length=25,
                            choices=RULES,
                            default=PON,verbose_name='Rules')
        bracket=models.CharField(max_length=25,
                            choices=BRACKET,
                            default=SE,verbose_name='Brackets')

        kids_special_formats=models.CharField(max_length=25,
                            choices=BRACKET,
                            default=SE,verbose_name='Kids Special Format')

        kids_special_rules=models.CharField(max_length=25,
                                choices=RULES,
                                default=PON,verbose_name='Kids Special Rules')




        gi=models.BooleanField(default=False,verbose_name='GI')
        nogi=models.BooleanField(default=False,verbose_name='NOGI')
        kids=models.BooleanField(default=False,verbose_name='KIDS')
        pro=models.BooleanField(default=False,verbose_name='PRO')
        purse=models.BooleanField(default=False,verbose_name='PURSE PRIZE')
        absolute=models.BooleanField(default=False,verbose_name='ABSOLUTE')
        adults=models.BooleanField(default=False,verbose_name='ADULTS')
        kids_special_format=models.BooleanField(default=False,verbose_name='KIDS SPECIAL FORMAT')


        cost=models.PositiveIntegerField(max_length=5,blank=True, null=True,verbose_name='Event Ticket Cost')
        predate=models.DateField(blank=True, null=True,verbose_name='Event Pre Date')
        cost_late=models.PositiveIntegerField(max_length=5,blank=True, null=True,verbose_name='Late Cost')
        cutoff_date=models.DateField(blank=True, null=True,verbose_name='Cut-off Date')
        event_description=models.TextField(max_length=5024,blank=True, null=True,verbose_name='Event Description')
        event_web = models.URLField(max_length=200, blank=True, verbose_name='Event Website')

        small_image=models.ImageField(upload_to='documents',default = 'documents/no-img.jpeg',verbose_name='Event Image(Small)')
        large_image=models.ImageField(upload_to='documents',default = 'documents/no-img.jpeg',verbose_name='Event Image(Large)')

        added = models.DateTimeField(auto_now_add=True,blank=True, null=True,verbose_name='Data Added')
        updated = models.DateTimeField(auto_now=True,blank=True, null=True,verbose_name='Data Updated')

        def image_tag(self):
          return mark_safe('<img src="%s" width="150" height="150" />' % (self.small_image.url))

        image_tag.short_description = 'Image'

        class Meta:
            verbose_name_plural = "Event Details"
