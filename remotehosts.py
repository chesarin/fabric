#!/usr/bin/env python
import getpass
from cuisine import *
from fabric.api import *

def read_hosts_file(filename=None):
    if not filename:
        filename = raw_input("Enter filename to read:")
    myhosts = []
    with open(filename,"r") as file:
        for host in file:
            myhosts.append(host)
    print 'Total number of entries in myhost is {}'.format(len(myhosts))
    return myhosts

env.hosts = read_hosts_file()
env.use_ssh_config = False


def update_package():
    password = getpass.getpass(prompt="Enter your sudo password:> ")
    sudo_password(password)
    select_package("yum")
    package = raw_input("What package would you like to upgrade:> ")
    upgrade = raw_input("Upgrading package should we continue Y/N?")
    package_ensure(package)
    if upgrade == "Y":
        package_update_yum(package)
    elif upgrade == "N":
        print "We are terminating without upgrading"
    else:
        print "I do not understand option {}".format(upgrade)

def restart_apache():
    httpd_service = "httpd"
    upstart_restart(httpd_service)

def stop_apache():
    httpd_service = "httpd"
    upstart_stop(httpd_service)