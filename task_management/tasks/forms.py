#-*- coding:utf-8-*-
from django import forms

class TaskForm(forms.Form):
	"""用于填写新任务的信息的表单"""
	param = forms.CharField(
		required=True,
		label="参数",
		error_messages={'required': '请输入参数'},
		widget=forms.TextInput(),
	)

	RADIO_CHOICES = (
            (1, "远程脚本"),
            (2, "Web服务"),         
            (3, "执行文件"),
    )

	task_type =  forms.ChoiceField(
		required=True,
		label="任务类型",
		widget=forms.RadioSelect(),
		choices=RADIO_CHOICES,
	)

	def clean(self):
		if not self.is_valid():
			raise forms.ValidationError("类型必选")
		else:
			cleaned_data = super(TaskForm, self).clean()
