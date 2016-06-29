from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from flowlendercms.models import EventDetail,Promoter


class EventDetailAdmin(ImportExportModelAdmin):
        list_display = ('event_name', 'promoter', 'date', 'location','city','added','updated')
        list_display_links = ('event_name', 'promoter')
        search_fields = ['event_name', 'promoter']
        list_filter = ('event_name', 'promoter', 'date')
        pass

class PromoterAdmin(ImportExportModelAdmin):

        list_display = ('promoter_name', 'promoter_web')
        search_fields = ['promoter_name']
        list_filter = ('promoter_name', 'promoter_web')
        pass


admin.site.register(Promoter,PromoterAdmin)
admin.site.register(EventDetail,EventDetailAdmin)
