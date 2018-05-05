from django.conf.urls import url, include
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),    
    url(r'^login$', views.login),
    url(r'^register$', views.register),
    url(r'^success$', views.success),
    url(r'^logout$', views.logout),
    url(r'^course/(?P<id>[0-9]+)$', views.course),
    url(r'^join/(?P<id>[0-9]+)$', views.join),
    url(r'^poke/(?P<id>[0-9]+)$', views.poke)
    # try to understand poke relationship
]