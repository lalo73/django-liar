#! coding: utf-8
from django.core.urlresolvers import resolve, Resolver404
from django.test import TestCase
from functools import partial


class TestUtils(TestCase):
    def test_resolve_url_of_valid_app(self):
        resolve('/some/valid/path/')

    def test_resolve_admin_site(self):
        resolve('/admin/')

    def test_resolve_url_of_invalid_app(self):
        resolver = partial(resolve, '/some/invalid/path/')
        self.assertRaises(Resolver404, resolver)