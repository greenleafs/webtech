# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import patterns, include, url

from qa.views import test, p404

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^/', p404, name='root'),
    url(r'^login/', p404, name='login'),
    url(r'^signup/', p404, name='signup'),
    url(r'^ask/', p404, name='ask'),
    url(r'^popular/', p404, name='popular'),
    url(r'^new/', p404, name='new'),
    url(r'^question/(?P<id>[0-9]+)/$', test, name='question'),
    url(r'^admin/', include(admin.site.urls)),
)
