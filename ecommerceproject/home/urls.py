from django.conf.urls import url
from . import views
 
urlpatterns = [
 url(r'^$', views.index, name='index'),
 url(r'^about/$', views.about, name='about'),
 url(r'^$', views.index, name='home'),
 url(r'^whoweare$', views.whoweare, name='whoweare'),
 url(r'^contact$', views.contact, name = 'contact'),
 url(r'^whoweare', views.whoweare, name = 'whoweare'),
 url(r'^sent', views.sent, name = 'sent'),
]