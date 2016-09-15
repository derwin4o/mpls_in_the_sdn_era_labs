#! /usr/bin/python
#from subprocess import call
#print(call(["ansible", "cisco", "-i", "hosts", "--list-hosts"]))
import sys
# 1. Imports
import pyansible.ansirunner
import pyansible.ansiInventory
import ansible
# 2. Using inventory.
myhostgroup = "cisco"
inventory = pyansible.ansiInventory.AnsibleInventory("./hosts")
if not inventory.get_hosts(myhostgroup):
    print "No host for group %s found " % myhostgroup
    sys.exit()
hostlist = inventory.get_hosts(myhostgroup[0]['hostlist'])
print hostlist





























