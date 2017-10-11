# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .models import Project


# Create your views here.

def index(request):
    projects = Project.objects.order_by('order_int')
    return render(request, 'hub/index.html', {'portfolio': projects})