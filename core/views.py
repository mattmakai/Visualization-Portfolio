from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime, date
from random import choice, sample
from core.models import Visualization
import json, re, urlparse


TEMPLATE_PATH = 'core/'

def _create_params(req):
    p = {}
    p.update(csrf(req))
    return p


def landing(req):
    p = _create_params(req)
    p['visualizations'] = Visualization.objects.all()
    return render(req, TEMPLATE_PATH + 'landing.html', p)

def visualization(req, slug):
    p = _create_params(req)
    p['visualizations'] = Visualization.objects.all()
    p['visualization'] = get_object_or_404(Visualization, slug=slug)
    return render(req, TEMPLATE_PATH + 'visualization.html', p)
