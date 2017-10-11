# Helper functions for the URL Shortener app

from ..models import URL
from django import forms
import string
import random

available_chars = string.ascii_letters + string.digits
chars_in_short_url = 5

def is_url(long_url):
    test_form = forms.URLField()
    try:
        test_form.clean(long_url)
        return True
    except:
        return False

def generate_rand_char():
    num_chars = len(available_chars)
    selection = random.randint(0, num_chars-1)
    return available_chars[selection]

def check_short_url(short_url):
    if not short_url:
        return False

    #Big potential bottleneck. Not sure if necessary with uniqueness active in
    #in the database, but doesn't hurt in small scale
    short_found = URL.objects.filter(short_url__exact=short_url)
    if short_found:
        return False
    return True

def check_long_url(long_url):
    if not long_url:
        return False

    try:
        long_found = URL.objects.filter(orig_url__exact=long_url).first()
        return long_found
    except:
        return False

def create_url(original_url, short_url=""):
    if not is_url(original_url):
        # Return -1 if provided long url is not a legitimate URL.
        return (-1, None)

    check_form = forms.URLField()
    long_url_clean = check_form.clean(original_url)
    long_checked = check_long_url(long_url_clean)

    if long_checked and short_url == "":
        # If the long url has already been shortened in the past AND user didn't
        # provide custom short, give the previously created URL.
        return (1, long_checked)

    if short_url:
        short_url = "".join(short_url.split())

    short_check_flag = check_short_url(short_url) # Done to save one check iteration.

    if short_url and not short_check_flag:
        # Return -2 if provided short URL has already been used.
        return (-2, None)

    while not short_check_flag:
        short_url = ""
        for i in range(chars_in_short_url):
            short_url += generate_rand_char()
        short_check_flag = check_short_url(short_url)

    new_url = URL.objects.create(orig_url = long_url_clean, short_url = short_url)
    return (2, new_url)


