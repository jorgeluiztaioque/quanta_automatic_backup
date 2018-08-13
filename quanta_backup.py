#!/usr/bin/env python3

from netmiko import ConnectHandler
import sys

ip = sys.argv[1]
user = sys.argv[2]
userPass = sys.argv[3]
enablePass = sys.argv[4]
port = sys.argv[5]
command = sys.argv[6]

quanta = {
	'device_type': 'hp_procurve',
	'ip':	ip,
	'username':	user,
	'password':	userPass,
	'secret':	enablePass,
	'port':	port,
	'verbose': False,
}

net_connect = ConnectHandler(**quanta)
net_connect.enable()
net_connect.find_prompt()
net_connect.send_command('terminal length 0')  
output = net_connect.send_command(command)
print (output)
	
net_connect.disconnect() 

