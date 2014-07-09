#-*- coding:utf-8-*-
from django.conf.urls import patterns,urls
from tasks import views

urlpatterns = patterns('',
	url(r'^$', views.list_tasks, name='list'))
)