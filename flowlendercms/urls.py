from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()generatefinal

urlpatterns = [
    # index page
    url(r'^login/$', flowlendercmsviews.user_login, name='login'),
    url(r'^$', 'flowlendercms.views.data', name='data'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
