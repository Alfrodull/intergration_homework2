#-*- coding:utf-8-*-

from django.db import models
from django.contrib.auth.models import User  

class Task(models.Model):
	"""任务类，每一个实例是用户提交的一个具体任务"""
	user = models.ForeignKey(User)
	task_type = models.IntegerField(blank = False)
	status = models.BooleanField(default = False)
	param = models.CharField(max_length = 200)
	pub_date = models.DateTimeField()