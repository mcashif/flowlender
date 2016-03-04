from django.contrib import admin
from flowlendercms.models import Feedback,Service,New,Contect,Apply
from flowlendercms.models import ClientDetail


class ClientDetailAdmin(admin.ModelAdmin):
        fieldsets = (
            (None, {
                'fields': ('business_name', 'reffering_party', 'data_date','payment_plan','ammount_request','debit_for','credit_score'
                ,'current_status', 'contact_name')
            }),
            ('More Contact Info', {
                'classes': ('collapse',),
                'fields': ('mailing_address', 'office_number','mobile_number', 'fax_number','email')
            }),
        )

        list_display = ('business_name', 'reffering_party', 'data_date', 'current_status','debit_ratio')
        list_display_links = ('business_name', 'reffering_party')
        search_fields = ['business_name', 'reffering_party']
        list_filter = ('business_name', 'reffering_party', 'current_status')

class FeedbackAdmin(admin.ModelAdmin):
        list_display = ('name','email','phone', 'data_date')
        search_fields = ['name', 'message']

# Register your models here.
admin.site.register(Service)
admin.site.register(New)
admin.site.register(Apply)
admin.site.register(Contect)
admin.site.register(Feedback,FeedbackAdmin)
admin.site.register(ClientDetail,ClientDetailAdmin)
