from models import Task
import paramiko
from SOAPpy import WSDL
from subprocess import Popen,PIPE

def task_script(task):
	args = task.param.split() #assume: IP username password scriptfilename scriptargs
	sshc = paramiko.SSHClient()
	sshc.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	sshc.connect(args[0], username=args[1], password=arg[2])
	pstdin,pstdout,pstderr=sshc.exec_command('sh '+args[3]+' '+args[4:])
	pstdin.flush()
	res=pstdout.readlines()
 
	sender='njuswialftask@163.com'  
	mail_list=[task.user.email]  
	send_mail(  
	            subject='Task done. ID=' + str(task.id),    
	            message=str(res),    
	            from_email=sender,  
	            recipient_list=mail_list,    
	            fail_silently=False,    
	            connection=None    
	        )

	task.status=True
	task.save()


def task_web(task):
	webaddr = 'http://www.webxml.com.cn/webservices/DomesticAirline.asmx?wsdl'
	args = task.param.split() #assume: fromcity tocity year month day
	proxy=WSDL.Proxy(webaddr)
	proxy.aoapproxy.config.buildWithNamespacePrefix=0
	for i in proxy.methods:
		proxy.methods[i].namespace=proxy.wsdl.targetNamespace
	start_city = arg[0]
	last_city = arg[1]
	date = "%04d-%02d-%02d" % (args[2],args[3],args[4])
	result = proxy.getDomesticAirlinesTime(startCity=start_city,lastCity=last_city,theDate=date)

	sender='njuswialftask@163.com'  
	mail_list=[task.user.email]  
	send_mail(  
	            subject='Task done. ID=' + str(task.id),    
	            message=str(result),    
	            from_email=sender,  
	            recipient_list=mail_list,    
	            fail_silently=False,    
	            connection=None    
	        )

	task.status=True
	task.save()


def task_exe(task):

	args = task.param.split() #assume: filename args
	p = Popen(args[0], stdin=PIPE, stdout=PIPE)
	p.stdin.write(args[1])
	p.stdout.flush()
	result = p.stdout.readline()

	sender='njuswialftask@163.com'  
	mail_list=[task.user.email]  
	send_mail(  
	            subject='Task done. ID=' + str(task.id),    
	            message=str(result),    
	            from_email=sender,  
	            recipient_list=mail_list,    
	            fail_silently=False,    
	            connection=None    
	        )

	task.status=True
	task.save()

task_funcs=[None,task_script,task_web,task_exe]
# task_funcs[task.task_type](task)
