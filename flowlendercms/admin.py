from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from flowlendercms.models import EventDetail,Promoter


class EventDetailAdmin(ImportExportModelAdmin):
        list_display = ('image_tag','event_name', 'event_promoter', 'event_date','event_geocode','added','updated')
        list_display_links = ('event_name', 'event_promoter')
        readonly_fields = ('image_tag',)
        search_fields = ['event_name', 'event_promoter']
        list_filter = ('event_name', 'event_promoter', 'event_date')
        date_hierarchy = 'event_date'
        ordering = ('-event_date',)

        fieldsets = [
        (None, {
                'fields': ['event_name', 'event_promoter', 'event_date', 'event_geocode','end_date']}),

        ('Address', {
                        'classes': ('collapse',),
                        'fields': ['location', 'address', 'city', 'state','zip_code']}),

        ('Rules & Brackets', {

                        'classes': ('collapse',),
                        'fields': ['rule', 'bracket', 'kids_special_formats', 'kids_special_rules']}),

        ('Catagories', {

                        'classes': ('collapse',),
                        'fields': ['gi', 'nogi', 'kids', 'pro', 'purse', 'absolute','adults', 'kids_special_format']}),

        ('Cost & Details', {

                        'classes': ('collapse',),
                        'fields': ['cost', 'predate', 'cost_late', 'cutoff_date','event_description']}),

        ('Images', {

                        'classes': ('collapse',),
                        'fields': ['small_image','large_image']}),
    ]

        pass

class PromoterAdmin(ImportExportModelAdmin):

        list_display = ('image_tag', 'promoter_name', 'promoter_web')
        readonly_fields = ('image_tag',)
        search_fields = ['promoter_name']
        list_filter = ('promoter_name', 'promoter_web')
        pass


admin.site.register(Promoter,PromoterAdmin)
admin.site.register(EventDetail,EventDetailAdmin)
