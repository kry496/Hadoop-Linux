# Hadoop-Linux
On-GOing-ProjectPython Automation Framework with Fabric for APACHE+HADOOP-2.7.3+Cluster deployement
""" Fab file created by prem = kry496@my.utsa.edu for Apache Hadoop Cluster deployment in Ubuntu or CentOs """

Deploy multi-node Apache Hadoop cluster with Fabric Library and Python
Fabric is a ssh/fscp/ftp/bash-login-shell wrapper to run commands on local and remote hosts
Project was built using Fabric 1.13 Package - Stable version as of Dec 2016
Tested on Ubuntu  ; support for CentOS/RHEL with SE will be added in few months
Create Terminalbox( install fabric here) to run your script

#some Rules:
All vms should be of same distribution, Currently it works on ubuntu
Hadoop related VMs - one MasterNode and ANY number of Slave nodes, use Virtual box. 
On virtual box -create the VMs with one Regular NAT adapter to use ur host os's Internet
and create one other network adapter with Virtual box host only mode
This way you get a pre interconnected Set of VMS
Pre-interconnected nodes or cluster with IP addresses on virtual adapter which we use.
use the Private IPs that are generated and add it to the env values in the scripts
Pre-requisites for the script to function ->  properly install fabric as root
use command -> pip install fabric==1.13     is the command that you need.
if its a new server(terminal-box) run the yum /apt upgrade before starting this script even the script calls it.



#Update : 
Tests complete on Ubuntu Nodes

#Features to be added to this project
 		Vagrantfile for the intial VM setups left to be added
		As the script runs as HDUSER, vagrant for the VMs is the best solution 






#---->>  setup the Python - fabric automation framework
if you never used the fabric library, read up a little.
For advanced users: with understanding of hadoop and fabric:
Ready made hadoop_config_files needs to stored in the terminal-box(where fabric is installed)  as per script
these files will be copied over to the hadoop nodes by the script
Until the VagrantFile is added
Set up VMs and install fabric 1.13 latest version
Set the host names like -> master, slave1, slave2 on the vms
Update the master and slave names in the slaves file of the hadoop config folder
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

