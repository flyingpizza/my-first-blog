from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login$', views.login, name='post_list'),
    url(r'^contactus',views.contactus, name='contactus'),
]