#!/bin/bash

echo "
1) Check Network Interface Information
2) Ping a Host
3) Port Scan with Nmap
4) Display Routing Table
5) Traceroute to Host
6) Exit"

echo "choose your option"

read varname

if [ $varname -eq 1 ]; then
ip a

elif [ $varname -eq 2 ]; then
ping 8.8.8.8

elif [ $varname -eq 3 ]; then
nmap 192.168.1.184 -sn

elif [ $varname -eq 4 ]; then
netstat -rn

elif [ $varname -eq 5 ]; then
traceroute 192.168.1.184

elif [ $varname -eq 6 ]; then
echo "exiting"


else
echo "option not valid.. exiting"

fi
