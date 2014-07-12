#-*- coding:utf-8-*-
from django.shortcuts import render_to_response,render,get_object_or_404  
from django.http import HttpResponse, HttpResponseRedirect  
from django.contrib.auth.models import User  
from django.contrib import auth
from django.contrib import messages
from django.template.context import RequestContext

from django.forms.formsets import formset_factory
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from tasks.models import Task

# from bootstrap_toolkit.widgets import BootstrapUneditableInput
from django.contrib.auth.decorators import login_required

from .forms import LoginForm

def login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render_to_response('userlogin/login.html', RequestContext(request, {'form': form,}))
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect("/tasks/")
            else:
                return render_to_response('userlogin/login.html', RequestContext(request, {'form': form,'password_is_wrong':True}))
        else:
            return render_to_response('userlogin/login.html', RequestContext(request, {'form': form,}))

@login_required  
def logout(request):  
    auth.logout(request)  
    return HttpResponseRedirect("/tasks/")
    # return HttpResponse(request.user.username)


@login_required
def detail(request):
    user = request.user

    task_list = user.task_set.all().order_by('-pub_date')
    my_task_list = []
    type_list = ['','远程脚本', 'Web服务', '执行文件']
    for task in task_list:
        tdic={}
        tdic["id"] = task.id
        tdic["task_type"] = type_list[task.task_type]
        if task.status:
            tdic["status"] = "完成"
        else: tdic["status"] = "未完成"
        tdic["param"] = task.param
        tdic["pub_date"] = task.pub_date
        my_task_list.append(tdic)
    context = {'my_task_list': my_task_list,
                'user': user}
    return render(request, 'userlogin/tasklist.html', context)  