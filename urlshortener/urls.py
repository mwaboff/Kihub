from django.conf.urls import url

from . import views

app_name = 'short'
urlpatterns = [
    #ex: /short/
        url(r'^$', views.index, name='index'),
    #ex: /short/create
        url(r'^api/create/$', views.create, name='create'),
    #ex: /short/i32s5/info
        url(r'^(?P<short_url>\w+)/info/$', views.info_viewer, name='info_viewer'),
    #ex: /short/i32s5
        url(r'^(?P<short_url>\w+)/$', views.redirector, name='redirect'),
]