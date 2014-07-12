#-*- coding:utf-8 -*-
from django.shortcuts import render,render_to_response
from django.template.context import RequestContext
from tasks.models import Task
from tasks.forms import TaskForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

def index(request):
	user = request.user

	task_list = Task.objects.order_by('-pub_date')
	latest_task_list = []
	type_list = ['','远程脚本', 'Web服务', '执行文件']
	for task in task_list:
		tdic={}
		tdic["id"] = task.id
		tdic["task_type"] = type_list[task.task_type]
		if task.status:
			tdic["status"] = "完成"
		else: tdic["status"] = "未完成"
		tdic["username"] = task.user.username
		tdic["pub_date"] = task.pub_date
		latest_task_list.append(tdic)
	context = {'latest_task_list': latest_task_list,
				'user': user}
	return render(request, 'tasks/index.html', context)

@login_required
def newtask(request):
	if request.method == 'GET':
		form = TaskForm()
		return render_to_response('tasks/newtask.html',
			RequestContext(request, {'form': form,}))
	else:
		form = TaskForm(request.POST)
		if form.is_valid():
			ttp = request.POST.get('task_type', 0)
			arg = request.POST.get('param', '')
			if ttp == 0:
				return render_to_response('tasks/newtask.html', \
				RequestContext(request, {'form': form,}))
			else:
				task = Task()
				task.task_type = ttp
				task.user = request.user
				task.param = arg
				task.pub_date = timezone.now()
				task.save()
				return HttpResponseRedirect("/tasks/")
		else:
			return render_to_response('tasks/newtask.html', 
				RequestContext(request,{'form':form}))