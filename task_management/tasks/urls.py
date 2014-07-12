#-*- coding:utf-8-*-
from django.conf.urls import patterns,url
from tasks import views
# from django.views.generic import ListView
from tasks.models import Task

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    # url(r'^$', 
    # 	ListView.as_view(
    # 		queryset=Task.objects.order_by('-pub_date'),
    # 		context_object_name='latest_task_list',
    # 		template_name='tasks/index.html'
    # 	),
    # name='index'
    # ),
	url(r'^new$', views.newtask, name='newtask'),
	url(r'^execute$', views.execute, name='execute'),
)