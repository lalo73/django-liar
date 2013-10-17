#! coding: utf-8
from django.conf.urls import patterns, include
from liar.utils import url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('invalidapp.urls')),
    url(r'^', include('validapp.urls')),
)