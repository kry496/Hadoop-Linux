# Hadoop-Linux
On-GOing-Project:HADOOP+Linux+ Python+Fabric+APACHE+HADOOP-2.7.3+Cluster
""" Fab file created by prem = kry496@my.utsa.edu for Apache Hadoop Cluster deployment in Ubuntu or CentOs """
# December 2016  # Deploy multi-node Apache Hadoop cluster with Python -Fabric Module 
#Fabric is a ssh/fscp/ftp/bash-login-shell wrapper to run commands on local and remote hosts
# Works with Fabric 1.13 on Ubuntu & CentOs ; support for RHEL with SE will be added 
# Create Terminalbox(control node) to run your script
# Hadoop related VMs - one MasterNode and Any number of Slave nodes, use Virtual box. 
# On virtual box when u create the VMs with Regular NAT adapter and other network adapter with
# with Virtual box host only mode, This way you get a pre interconnected
# Pre-interconnected nodes or cluster with IP addresses automatically assigned on Virtual Adapters
# use the Private IPs that are generated and add it to the env values in the scripts
#Pre-requisites for the script to function ->  properly install fabric as root
# use command -> pip install fabric==1.13     is the command that you need.
# if its a new server(terminal-box) run the yum /apt upgrade before starting this script even the script calls it.


