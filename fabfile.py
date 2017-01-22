
""" Fab file created by Kry496@my.utsa.edu for Apache Hadoop Cluster deployment in Ubuntu or CentOs """
# December 2016
# Works on Fabric 1.13 and Ubuntu & CentOs ; support for RHEL with SE will be added 
# MasterNode and Slave nodes, use Virtual box. On Each node: one adapter goes to internet and other internal network with static routing
# Pre-requisites for the script to function properly install fabric as root
# pip install fabric==1.13     is the command that you need.
# if its a new server run the yum /apt upgrade before starting this script even the script calls it.


# import all the fabric functions that we need explicitly
from fabric.api import env, roles, sudo, execute, put, run, local, lcd, prompt, cd, parallel, settings, hide, quiet 
from fabric.contrib.files import exists, append, contains
import fabric.operations
# import platform module to test the machine type.
# Non Fabric library fabric related imports: import entire module to enable code & namespace management at scale.

import platform

# import the os module to get file basenames

import os

# import String for appeding string data to files

import StringIO

# import exists, append, contains 

from fabric.contrib.files import exists,append,contains



#add to bash file

bashrc_updates = """
#add to bash file 
# Set Hadoop-related environment variables
export HADOOP_HOME=/usr/local/hadoop/hadoop
export HADOOP_MAPRED_HOME=$HADOOP_HOME
export HADOOP_COMMON_HOME=$HADOOP_HOME
export HADOOP_HDFS_HOME=$HADOOP_HOME
export YARN_HOME=$HADOOP_HOME
export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
export HADOOP_JAR=/usr/local/hadoop/hadoop/share/hadoop/mapreduce
# Set JAVA_HOME (we will also configure JAVA_HOME directly for Hadoop later on)
export JAVA_HOME=/usr/lib/jvm/default-java

# Some convenient aliases and functions for running Hadoop-related commands
#unalias fs &> /dev/null
#alias fs="hdfs"
#unalias hls &> /dev/null
#alias hls="fs -ls"


# If you have LZO compression enabled in your Hadoop cluster and
# compress job outputs with LZOP (not covered in this tutorial):
# Conveniently inspect an LZOP compressed file from the command
# line; run via:
#
# $ lzohead /hdfs/path/to/lzop/compressed/file.lzo
# Note : we are not compressing  !!!!!!  Yet !!!!
# Requires installed 'lzop' command.
#

# Add Hadoop bin/ directory to PATH

export PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin

"""

# Update the Roledef environment variable to define the set of master and slave nodes for the hadoop configuration.
env.roledefs = {
    'masternode': ['192.168.56.122'],
    'slavenodes': ['192.168.56.121', '192.168.56.126'],
}

# List Comprehension to define all sevever in a single list to apply certain settings to all servers 
env.roledefs['all'] = [x for y in env.roledefs.values() for x in y]

#add to /etc/hosts file

hosts_file_update='''
192.168.56.122 master
192.168.56.126 slave1
192.168.56.121 slave2

'''
#disable ipv6

sysctl_update='''
net.ipv6.conf.all.disable_ipv6 = 1
net.ipv6.conf.default.disable_ipv6 = 1
net.ipv6.conf.lo.disable_ipv6 = 1'''



# Define the list of packages required. # setting up the dictionary for scaling the script.
#packages_required = {
#   'masternode': ['default-jdk','openssh-server',],
#   'slavenodes': ['default-jdk','openssh-server',]
#}
#
env.user='hduser'
env.sudo_password='Lab1lab2'

# lets create a hadoop user 
#      @parallel
@roles('all')
def create_hduser():
	if run('id -u hduser', warn_only=True).return_code == 1:
		sudo('addgroup hadoopadmin && adduser --ingroup hadoopadmin hduser && usermod -aG sudo hduser', pty=True)
	else:
		print " hduser exists"

		
# The hadoop Mapreduce test files and hadoop 2.7.3 tar files that need to be downloaded
test_files = {
    'masternode' : ['http://www.gutenberg.org/ebooks/20417',
                    'http://www.gutenberg.org/ebooks/5000',
					'http://www.gutenberg.org/ebooks/4300',
					]
					}

download_hadoop = {
	'masternode' : ['http://www-eu.apache.org/dist/hadoop/core/hadoop-2.7.3/hadoop-2.7.3.tar.gz']
}


#download the files with the function

@roles('masternode')
def download_files():
	hadoop_dir = "/usr/local/hadoop"
	if not exists('usr/local/hadoop', use_sudo=True):
		sudo('mkdir -p %s' %hadoop_dir, pty=True)
		sudo('chown hduser:hadoopadmin %s' % hadoop_dir, pty=True)
		sudo('chmod g+s %s' %hadoop_dir, pty=True)
	with cd(hadoop_dir):
		for url in download_hadoop['masternode']:
			filename = "%s/%s" %(hadoop_dir, os.path.basename(url))
			sudo('wget --no-cache %s -O %s' %(url, filename), pty=True)
	

@roles('masternode')
def download_test_files():
	test_dir = '/home/hduser/test'
	if not exists('/home/hduser/test/(*?).*', use_sudo=True):
		sudo('mkdir -p %s' %test_dir, pty=True)
		sudo('chown -R hduser:hadoopadmin %s' %test_dir, pty=True)
		sudo('chmod g+s %s' %test_dir, pty=True)
		with cd(test_dir):
			for url in test_files['masternode']:
				testfilename = "%s/%s" %(test_dir, os.path.basename(url))
				sudo('wget --no-cache %s -O %s' %(url, testfilename), pty=True)






 		 
# Install JDK depending on the linux distribution

def _java_distro():
	with settings (warn_only=True):
		if 'ubuntu' in platform.platform().lower():
			sudo('apt-get -y install default-jdk')
		elif 'centos' in platform.platform().lower():
			sudo('yum install -y default-jdk')
		else:
                        print 'this script works only on ubuntu or centos linux distribution'
			print 'exiting the script'




@parallel			
@roles('all')	
def  java_install():
	with quiet():
		a =  run('which java')
       		if a.return_code >= 1:
        		_java_distro()
	        elif a.return_code  == 0:
	        	print ' java is installed'
		else:
			print 'unknown return_code'
	
@roles('masternode')
def create_ssh_key():
	with settings (warn_only=True):
		sudo('ssh-keygen -t rsa -P"" -f /home/hduser/.ssh/id_rsa')
		sudo("cat /home/hduser/.ssh/id_rsa.pub >> /home/hduser/.ssh/authorized_keys")
		sudo("chmod 600 /home/hduser/.ssh/authorized_keys")
		

@roles('slavenodes')
def copy_ssh_key():
	with settings (warn_only=True):
		sudo('ssh-keygen -t rsa -P "" -f /home/hduser/.ssh/id_rsa')
		sudo("cat /home/hduser/.ssh/id_rsa.pub >> /home/hduser/.ssh/authorized_keys")
		sudo("chmod 0600 /home/hduser/.ssh/authorized_keys")
		sudo("ssh-keyscan -H master >> /home/hduser/.ssh/known_hosts")
		
		


# lets append the bashrc_updates text to the bashrc file of HDUSER
# fabric.contrib.files.append(filename, text, use_sudo=False, partial=False, escape=True, shell=False)
# even with settings (sudo_user .... we need to specify the parameters above for the command to go through)


@parallel				  
@roles('all')
def update_bashrc():
	with settings (warn_only=True):
		if exists('/home/hduser/.bashrc', use_sudo=True):
			if not contains('/home/hduser/.bashrc', "HADOOP"):
				append('/home/hduser/.bashrc', bashrc_updates, use_sudo=True)
				sudo('source /home/hduser/.bashrc', pty=True)
			else:
				print " HADOOP ENVs are already updated"
		else:
			print 'hduser doesnt exist'

@parallel				  
@roles('all')
def update_hostfile():
	with settings (warn_only=True):
		if not contains('/etc/hosts', 'master'):
			append('/etc/hosts', hosts_file_update, use_sudo=True)
		else:
			print ' the etc host file is already updated'

@parallel
@roles('all')
def disable_ipv6():
	with settings (warn_only=True):
		if not contains('/proc/sys/net/ipv6/conf/all/disable_ipv6', '1'):
			append('/etc/sysctl.conf', sysctl_update, use_sudo=True)
			sudo('sysctl -p', pty=True)
		else:
			print 'IPV6 is already disable'
		

@parallel
@roles("all") # this decorater will make the the function following it  run for all servers
def upgrade_servers():
	if 'ubuntu' in platform.platform().lower:
		sudo('apt-get upgrade')
	elif 'centos' in platform.platform().lower:
		sudo("yum -y upgrade",pty=True)
	else:
        	print 'this script works only on ubuntu or centos linux distribution'
		print 'exiting the script'



# this is the main function we will be calling to get it all running
def deploy():
    # note here that the execute function has the names of the functions we
    # are calling, but we are excluding the parenthesis()
    execute(upgrade_servers)
    execute(create_hduser)
    execute(java_install)
    execute(copy_ssh_key)	
    execute(update_bashrc)
    execute(update_hostfile)
    execute(disable_ipv6)

