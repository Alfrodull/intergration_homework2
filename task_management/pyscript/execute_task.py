#-*- coding:utf-8 -*-
import sys,string
import paramiko
from SOAPpy import WSDL
from subprocess import Popen,PIPE

def task_script(args):
	#assume parametes: IP username password scriptfilename scriptargs
	sshc = paramiko.SSHClient()
	sshc.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	sshc.connect(args[0], username=args[1], password=arg[2])
	pstdin,pstdout,pstderr=sshc.exec_command('sh '+args[3]+' '+args[4:])
	pstdin.flush()
	res=pstdout.readlines()
	print res
 


def task_web(args):
	webaddr = 'http://www.webxml.com.cn/webservices/DomesticAirline.asmx?wsdl'
	#assume parametes: fromcity tocity year month day
	proxy=WSDL.Proxy(webaddr)
	proxy.soapproxy.config.buildWithNamespacePrefix=0
	for i in proxy.methods:
		proxy.methods[i].namespace=proxy.wsdl.targetNamespace
	start_city = args[0].decode('utf8')
	last_city = args[1].decode('utf8')
	date = "%04d-%02d-%02d" % (string.atoi(args[2]),string.atoi(args[3]),string.atoi(args[4]))
	result = proxy.getDomesticAirlinesTime(startCity=start_city,lastCity=last_city,theDate=date)
	# print result
	for i in result[1].Airlines.AirlinesTime:
		print i.Company
		print i.AirlineCode
		print i.StartDrome
		print i.ArriveDrome
		print i.Mode
		print i.AirlineStop
		print i.Week
		print '\n'



def task_exe(args):

	#assume parametes: filename args
	p = Popen(args[0], stdin=PIPE, stdout=PIPE)
	p.stdin.write(args[1])
	p.stdout.flush()
	result = p.stdout.readline()
	print result


# task_funcs=[None,task_script,task_web,task_exe]
task_funcs = {
	'1':task_script,
	'2':task_web,
	'3':task_exe,
}
# task_funcs[task.task_type](args)

if __name__ == '__main__':
	task_funcs[sys.argv[1]](sys.argv[2:])