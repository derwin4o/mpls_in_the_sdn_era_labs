#!/usr/bin/python

from subprocess import call # for executing instersnal command which gives hosts from inventory file
import sys # to be able to take command line arguments
import paramiko
import time
host = sys.argv[1]
user = "rado"
key_filename = "/home/rado/.ssh/z-id_rsa"
tftp_link = sys.argv[2]
dest_file = "1.cfg"

print tftp_link
print dest_file

k = paramiko.RSAKey.from_private_key_file(key_filename)
group = "cisco"
c = paramiko.SSHClient()
c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print "connecting"
c.connect( hostname = host, username = user, pkey = k )
print "connected"
remote_conn = c.invoke_shell()
output = remote_conn.recv(65535)
print output
commands = [
    "copy "+tftp_link+" "+dest_file+"\n",
    "\n",
    "configure\n",
    "load disk0:"+dest_file+"\n",
    "commit replace\n",
    "yes\n"
]   	
print commands
for comm in commands: 
    remote_conn.send(comm)
    time.sleep(3)
    output = remote_conn.recv(65535)
print output


