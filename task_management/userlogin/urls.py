#-*- coding:utf-8-*-
from django.conf.urls import patterns,url
from userlogin import views

urlpatterns = patterns('',
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
	url(r'^detail/$', views.detail, name='detail'),
)