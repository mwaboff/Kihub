# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import URL
from .scripts.url_helper import create_url

# Create your views here.

def index(request):
    return render(request, 'urlshortener/index.html')

def redirector(request, short_url):
    found_URL_obj = get_object_or_404(URL, short_url=short_url)
    found_URL_obj.views += 1
    found_URL_obj.save()
    long_url = found_URL_obj.orig_url
    return HttpResponseRedirect(long_url)
    #return HttpResponse("You're on the redirect page for id=%s. The long_url = %s" % (short_url, long_url))

def info_viewer(request, short_url):
    found_URL_obj = get_object_or_404(URL, short_url=short_url)
    url_info = {
        'short_addr': found_URL_obj,
        'short_url': short_url,
        'long_url': found_URL_obj.orig_url,
        'views': found_URL_obj.views,
        'create_date': found_URL_obj.creation_date
    }
    return render(request, 'urlshortener/info.html', url_info)
    #return HttpResponse("You're on the info page for id=%s" % short_url)

def create(request):
    long_url = request.POST['long_url'].strip()
    short_url = request.POST['short_url'].strip()
    
    new_url = create_url(long_url, short_url)
    if new_url[0] == -1:
        error_info = {
            'success': -1,
            'message': "You dun goofed up. Make sure you put a valid URL in!"
        }
        return JsonResponse(error_info)
    elif new_url[0] == -2:
        error_info = {
            'success': 0,
            'message': "This short URL has already been taken, try another or keep it blank."
        }
        return JsonResponse(error_info)
    else:
        url_info = {
            'success': new_url[0],
            'short_addr': str(new_url[1]),
            'short_url': new_url[1].short_url,
            'long_url': new_url[1].orig_url,
        }

        return JsonResponse(url_info)