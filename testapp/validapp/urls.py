#! coding: utf-8
from django.conf.urls import patterns, include, url
from django.http import HttpResponse


def view(request, *args, **kwargs):
    return HttpResponse('This works!')

urlpatterns = patterns(
    '',
    url(r'^some/valid/path/$', view),
)