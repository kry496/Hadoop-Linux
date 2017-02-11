# Hadoop-Linux-Python-FABRIC
# ON-GOING-PROJECT    
Python Automation Framework with Fabric for APACHE+HADOOP-2.7.3+Cluster deployement.
""" Fab file created by prem = kry496@my.utsa.edu for Apache Hadoop Cluster deployment in Ubuntu or CentOs """

# Version of the fabfile.py found on github is the stable version of the code as of Jan 2017.
	- Multiple updates will be rolled into a single update by March 2017.
	- Vagrant file pending, Security updates pending

# Deploy multi-node Apache Hadoop cluster with Fabric Library and Python
	#Fabric is a ssh/fscp/ftp/bash-login-shell wrapper to run commands on local and remote hosts. 
	Project was built using Fabric 1.13 Package - Stable version as of Dec 2016
	Tested on Ubuntu  ; support for CentOS/RHEL with SE will be added in few months 
	Create Terminalbox( install fabric here) to run your script											
# Some Rules & Super Key Info :
	All vms should be of same distribution, Currently it works on ubuntu\n
	Hadoop related VMs - one MasterNode and ANY number of Slave nodes, use Virtual box. 
	On virtual box -create the VMs with one Regular NAT adapter to use ur host os's Internet
	and create one other network adapter with Virtual box host only mode
	This way you get a pre interconnected Set of VMS, which can talk to each other ; No need for DNS ; No need to set static IPs
	Pre-inteconnected nodes or cluster with IP addresses on virtual adapter which we use.
	use the Private IPs that are generated and add it to the env values in the scripts
	Pre-requisites for the script to function ->  properly install fabric as root
	use command -> pip install fabric==1.13     is the command that you need.
	if its a new server(terminal-box) run the yum /apt upgrade before starting this script even the script calls it.



# Update : 
	Tests complete on Ubuntu Nodes as of Jan 3rd week - 2017
	Next set of updates are set for March 2017.

# Features to be added to this project
 		Vagrantfile for the intial VM setups left to be added
		As the script runs as HDUSER, vagrant for the VMs is the best solution 

# ---->>  setup the Python - fabric automation framework
	if you never used the fabric library, read up a little :)
	For advanced users: with understanding of Hadoop and fabric:
	Ready made Hadoop_config_files ( from my github) needs to stored in the terminal-box(where fabric is installed)  
	You can locate this function, if you are not sure where it is stored
	these files will be copied over to the Hadoop Master & Slave nodes by the script
	Until the VagrantFile is added
	Set up VMs and install fabric 1.13 latest version ( Only on the terminal box) which is outside the Hadoop cluster
	Set the host names like -> master, slave1, slave2 on the vms that belong to the Hadoop cluster
	Update the master and slave names in the slaves file of the hadoop config folder ( that you downloaded from my git)(
	Edit the ips address on the script( in roledefs and add to host file variable
	Set up openssh-server on the vms, 
	Sset permitlogin as yes and strictmode to no in the sshd config file in the etc folder
	Disable firewall with the fab disable_firewall , (temporary work around)
	Functions for appropriate firewall settings will be added
	Important: For Intial user creation, comment out the env.user variable in script and run fab create_hduser
	Enter root password of the VMs, Once
	Once the Users are created ( u will need the credentials to run the script as hduser)
	Once HDUSER is created, uncomment the env.user variable and start the deployement with the command -->> fab deploy
	Script will install,start and test  Hadoop, on the IPs you set on  the roledef variables in script
	script will prompt u for password for intital ssh configs and before the cluster starts

# Final Thoughts:
	If you understand the Fabric library, All the comments should get you going 
	Keep the Program logic in Python; Thats the magic here ! Reason I love this tool
	letting Fabric be the wrapper to carry the commands to all the host & the host groups defined;
	The reason why we run the script as HDUSER; 
	The ERROR handling functionality is basic, 
	I have used the classic method ; not using @task decorator  ; going for single flat namespace to get the job done.
	
	

