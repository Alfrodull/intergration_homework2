#-*- coding:utf-8-*-

from django.db import models

class Task(models.Model):
	"""任务类，每一个实例是用户提交的一个具体任务"""
	task_type = models.IntegerField(blank = False)
	status = models.BooleanField(default = False)
	param = models.CharField(max_length = 200)
	pub_date = models.DateTimeField()