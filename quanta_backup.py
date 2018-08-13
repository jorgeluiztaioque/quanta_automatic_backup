#!/usr/bin/env python3

from netmiko import ConnectHandler
import sys

__author__ = 'Jorge Luiz Taioque'
__version__= 0.1

def main(argv):
	if not argv:
		print ('Usage:')
		print ('./quanta_backup.py [ipaddress] [user] [user_password] [enable_password] [ssh_port] [command]')
		print ('./quanta_backup.py 10.0.0.1 admin 123456 123456 22 "show running-config"')
	else:
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

if __name__ =='__main__':
    main(sys.argv[1:])
