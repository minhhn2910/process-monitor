#!/usr/bin/env python
import os
import sys
import time

def main (arguments):
	loop_interval = 30
	if len(arguments) < 1:
		print 'loop interval in minutes is not set, default is 30 mins'
	else:
		loop_interval = int(sys.argv[1])
		print 'running with loop interval = ' + str(loop_interval)
	while True:
		clean_job()
		time.sleep(loop_interval*60)
	pass
	
def clean_job():
	log_file = 'clean_job_log'
	config_file = 'clean_job_config'
        print "reading configuration from "+ config_file
        try:
		config = open(config_file)
		for line in config.readlines():
        	        arg = line.split()
        	        if len(arg) > 1:
        	                if arg[0] == 'percent_to_kill':
					percent_to_kill = float(arg[1])
				if arg[0] == 'minutes_to_kill':
					minutes_to_kill = float(arg[1])
	except IOError:
		print 'cannot read configurations from clean_job_config file, all configurations are set to default'
		percent_to_kill = 90
		minutes_to_kill = 30
	print 'clean job is running, will kill processes consume over ' + str(percent_to_kill) + ' after ' + str(minutes_to_kill) + ' minutes'
	os.system("top -b -n1  > top_result")
	file = open('top_result')
	log_file = open(log_file,'a')
	start = 0
	for line in file.readlines():
		a = line.split()
		if len(a) > 1:
			if start == 1:
				pid = a[0]
				user = a[1]
				cpu = float(a[8])
				time = a[10].split(':')[0]
				#print pid + ' ' + user + ' ' + str(cpu) + ' ' + time
				if user!='root' and cpu > percent_to_kill and time > minutes_to_kill :
					operation_string =  'kill '+ str(pid)
					print operation_string
					log_file.write(time.ctime()+ '   ' + operationg_string+ '   from  user: '+user+'\n')	
					os.system('kill '+ str(pid) )
			
			if a[0] == 'PID':
				start = 1
	log_file.close()

if __name__ == '__main__':
	main(sys.argv[1:])
		
