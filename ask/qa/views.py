# -*- coding: utf-8 -*-
"""QA application."""
from __future__ import unicode_literals

# from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404


# Create your views here.
def test(request, *args, **kwargs):
    """Test view."""
    return HttpResponse('OK')


def p404(request, *args, **kwargs):
    """."""
    raise Http404
