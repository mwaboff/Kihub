from django.conf.urls import url

from . import views

app_name = 'hub'
urlpatterns = [
    #ex: mwaboff.com
        url(r'^', views.index, name='index'),
]