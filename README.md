System utility to kill intensive cpu consuming processes

Configurable parameters in clean_job_conf file 
	percent_to_kill : the upperbound for filter (any proccesses using cpu more than this value will be taken into account)
	minutes_to_kill : processes that ran after this number of minutes will be taken into account

Usage:

Run under root privilege:

chmod +x monitor.py

./monitor.py [loop_interval]

TO DISABLE OUTPUT AND RUN AS A SERVICE; USING THIS COMMAND:

nohup ./monitor.py [loop_interval] &

this program will clean the system again after loop_interval minutes, default value is 30 minutes

	
