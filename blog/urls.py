from . import views
from django.conf.urls import patterns, include, url
from .views import *
from django.contrib.auth.views import login
urlpatterns = [
    url(r'^list/$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name = 'post_detail'),
    url(r'^post_new/$', views.post_new, name = 'post_new'),
    url(r'^topic/(?P<topic_pk>\w+?)/$', views.topic, name = 'topic'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'), 
    url(r'^subscribe/(?P<sub_pk>\w+?)/$', views.subscribe, name='subscribe'),
    url(r'^subscriptions/$', views.subscriptions, name='subscriptions'),

    url(r'^$', login),
    url(r'^logout/$', logout_page),
    url(r'^accounts/login/$', login), # If user is not login it will redirect to login page
    url(r'^register/$', register),
    url(r'^success/$', register_success),
    url(r'^home/$', home),
    url(r'^about/$', about),

]


