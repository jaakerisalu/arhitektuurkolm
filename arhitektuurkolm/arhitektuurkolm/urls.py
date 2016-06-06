from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import redirect

admin.autodiscover()


def __redirect_to_edit(request):
    return redirect('/edit/')


urlpatterns = [
    url(r'', include('accounts.urls')),
    url(r'^$', __redirect_to_edit),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^edit/', include(admin.site.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if not settings.DEBUG:
    handler500 = 'arhitektuurkolm.views.server_error'
    handler404 = 'arhitektuurkolm.views.page_not_found'
