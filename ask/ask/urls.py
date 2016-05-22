# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import patterns, include, url

from qa.views import (
    test,
    home,
    popular,
    question,
    ask,
    answer,
    signup,
    login_user,
    logout_user
)

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', home, name='root'),
    url(r'^login/$', login_user, name='login'),
    url(r'^logout/$', logout_user, name='logout'),
    url(r'^signup/$', signup, name='signup'),
    url(r'^ask/$', ask, name='ask'),
    url(r'^answer/$', answer, name='answer'),
    url(r'^popular/$', popular, name='popular'),
    url(r'^new/', test, name='new'),
    url(r'^question/(?P<id>.*)/$', question, name='question'),
    url(r'^admin/', include(admin.site.urls)),
)
