# Hadoop-Linux
On-GOing-ProjectPython Automation Framework with Fabric for APACHE+HADOOP-2.7.3+Cluster deployement
""" Fab file created by prem = kry496@my.utsa.edu for Apache Hadoop Cluster deployment in Ubuntu or CentOs """
# Tests complete on Ubuntu Nodes
#---->>  setup the Python - fabric automation framework
# if you never used the fabric library
# there are some intial instructions in the fab file as well part of the  pre-requisites.
#FOr advanced users: with understanding of hadoop and fabric:
# ready made hadoop_config_files needs to stored in the terminal-box(where fabric is installed)  as per script
# these files will be copied over to the hadoop nodes by the script
#Set up VMs and install fabric 1.13 latest version
# Vagrant for the intial VM setups left to be added
#set the host names like -> master, slave1, slave2 on the vms
# update the master and slave names in the slaves file of the hadoop config folder
#edit the ips address on the script( in roledefs and add to host file variable
# set up openssh-server on the vms, 
# set permitlogin as yes and strictmode to no in the sshd config file in the etc folder
# disable firewall with the fab disable_firewall , (temporary work around)
# Functions for appropriate firewall settings will be added
# Important: For Intial user creation, comment out the env.user variable in script and run fab create_hduser
# Enter root password of the VMs, Once
# Once the Users are created ( u will need the credentials to run the script as hduser)
# Once HDUSER is created, uncomment the env.user variable and start the deployement with the command -->> fab deploy
# Script will install,start and test  Hadoop, on the IPs you set on  the roledef variables in script
# script will prompt u for password for intital ssh configs and before the cluster starts
#script once the user is setup will automatically install the required packages
#disable ipv6, create the folders required, download hadoop 2.7.3 and install it
# format the name node, setup hdfs, and rest of the hadoop services
# and kick start the hadoop cluster 
# then it will run a test word count program on the hadoop cluster using three text files it downloads
# and store the result back in the test folder of the hduser on the master node.

