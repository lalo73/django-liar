#! coding: utf-8
from django.conf.urls import patterns, include, url
from django.http import HttpResponse, Http404


def view(request):
    return HttpResponse('This does not work!')


urlpatterns = patterns(
    '',
    url(r'^some/invalid/path/$', view),
)