from os import system
from platform import platform
from fabric.api import settings
from fabric.context_managers import  hide, quiet

def java_version():
#	with settings(hide('user', 'stdout')):
	with quiet():
		_java_fun()


def _java_fun():
	if system("which java") >= 1:
		if 'ubuntu' in platform().lower:
			system(" sudo apt-get -y install default-jdk")
		elif 'centos' in platform().lower:
			system(" sudo yum install -y default-jdk")
		else:
			print "this script works only on ubuntu or centos linux distribution"
	else:
		print "java is already installed"


