from django.conf.urls.defaults import *
from django.conf import settings

from django.views.generic.simple import direct_to_template

#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^', include('apps.social.urls', namespace='social')),
    (r'^cam/', include('apps.cam.urls', namespace='cam')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                            { 'document_root': settings.MEDIA_ROOT }),
        #(r'^admin-media/(?P<path>.*)$', 'django.views.static.serve',
        #                    {'document_root': settings.ADMIN_MEDIA_ROOT }),
    )
