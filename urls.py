from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('',

    (r'^', include('apps.social.urls', namespace='social')),
    (r'^cam/', include('apps.cam.urls', namespace='cam')),
    (r'^messages/', include('apps.user_messages.urls', namespace='user_messages')),
    (r'^notes/', include('apps.notes.urls', namespace='notes')),
    (r'^billing/', include('apps.billing.urls', namespace='billing')),
    url(r'^pay/pskb/$', 'apps.billing.views.operator', name='operator'),
    (r'^library/', include('apps.media_library.urls', namespace='media_library')),
    (r'^file/', include('apps.media.urls', namespace='media')),
    (r'^groups/', include('apps.groups.urls', namespace='groups')),
    (r'^friends/', include('apps.friends.urls', namespace='friends')),
    url(r'^in_dev/$', 'django.views.generic.simple.direct_to_template', name='in_dev', kwargs={'template': 'in_dev.html'}),
    url(r'^agreement/$', 'django.views.generic.simple.direct_to_template', name='agreement', kwargs={'template': 'agreement.html'}),

)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                            { 'document_root': settings.MEDIA_ROOT }),
        #(r'^admin-media/(?P<path>.*)$', 'django.views.static.serve',
        #                    {'document_root': settings.ADMIN_MEDIA_ROOT }),
    )
