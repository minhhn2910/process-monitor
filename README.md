System utility to kill intensive cpu consuming processes

Configurable parameters in clean_job_conf file 
	percent_to_kill : the upperbound for filter (any proccesses using cpu more than this value will be taken into account)
	minutes_to_kill : processes that ran after this number of minutes will be taken into account

Usage:

run under root privilege

./monitor.py x

x is the loop interval, this program will clean the system again after x minutes

	
