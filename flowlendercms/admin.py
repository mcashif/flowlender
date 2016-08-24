from django.contrib import admin
from flowlendercms.models import ClientDetail
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from flowlendercms.models import Profile

class UserProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (UserProfileInline, )



class ClientDetailAdmin(ImportExportModelAdmin):
        fieldsets = (
            (None, {
                'fields': ('business_name', 'reffering_party', 'data_date','payment_plan','ammount_request','debit_for','credit_score',
                'debit_ratio','current_status', 'contact_name')
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
        pass

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(ClientDetail,ClientDetailAdmin)
