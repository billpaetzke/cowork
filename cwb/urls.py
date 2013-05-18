from django.conf.urls import patterns, include, url

import spaces.views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cwb.views.home', name='home'),
    # url(r'^cwb/', include('cwb.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^cwb-admin/', include(admin.site.urls)),

    url(r'^$', spaces.views.HomeView.as_view(),
        name='spaces-home'),

    url(r'^search$', spaces.views.ListSpaceView.as_view(),
        name='spaces-search'),

    url(r'^new$', spaces.views.CreateSpaceView.as_view(),
        name='spaces-new'),

    url(r'^(?P<slug>[-\w\d]+),(?P<pk>\d+)/$', spaces.views.SpaceView.as_view(),
        name='spaces-view'),
)
