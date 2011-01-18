# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('apps.themes.views',
   url(r'^(?P<theme_id>[a-f0-9]{24})/(?P<file_name>[\w\.]+)$',
       'file_view', name='file_view'),
   url(r'^all/$', 'list', name='list'),
   url(r'^add/$', 'add', name='add'),
   url(r'^(?P<theme_id>[a-f0-9]{24})/delete/$', 'delete', name='delete'),

)