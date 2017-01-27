# Hadoop-Linux
On-GOing-Project:HADOOP+Linux+ Python+Fabric+APACHE+HADOOP-2.7.3+Cluster
""" Fab file created by prem = kry496@my.utsa.edu for Apache Hadoop Cluster deployment in Ubuntu or CentOs """
# you to setup the Python - fabric automation framework
# there are some intial instructions in the fab file as well, read them first.
# ready made hadoop_config_files needs to stored in the terminal-box as per script
# these files will be copied over the nodes by the script
#Set up VMs and fabric instructed on the fab file.
#remeber to set the host names like -> master, slave1, slave2 on the vms
#rememeber to set the ips address on the script( in roledefs and add to host file variable
# remember to set up openssh-server on the vms
# remember to set permitlogin as yes and strictmode to no in the sshd config file in the etc folder
# For Intial user creation, comment out the env.user variable in script and run fab create_hduser
# Enter root password of the VMs
# Once the Users are created ( u will need the credentials to run the script as hduser)
# currently you need to disable firewall before u run the script
# run  --> fab disable_rirewall and then  ->> fab reboot vms
# script to load appropriate firewall settings is being written
#script once all this is done, uncomment the env.user variable and start the deployement with
# # read everything and then run->> fab deploy
# Script will install,start and test  Hadoop, on the IPs you set on  the roledef variables in script
# script will prompt u for password for intital ssh configs and before the cluster starts
#script once the user is setup will automatically install the required packages
#disable ipv6, create the folders required, download hadoop 2.7.3 and install it
# format the name node, setup hdfs, and rest of the hadoop services
# and kick start the hadoop cluster 
# then it will run a test word count program on the hadoop cluster using three text files it downloads
# and store the result back in the test folder of the hduser on the master node.

