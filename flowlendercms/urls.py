from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()generatefinal

urlpatterns = [
    # index page
    url(r'^$', 'flowlendercms.views.index', name='index'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
