#!/bin/bash

echo "1) Check Network Interface Information
2) Ping a Host
3) Port Scan with Nmap
4) Display Routing Table
5) Traceroute to Host
6) Exit"

echo "choose an option: "

read varname

if [ $varname -eq 1 ]; then
ip a

elif [ $varname -eq 2 ]; then
read -p "inriduce pig destination" x
ping $x

elif [ $varname -eq 3 ]; then
read -p "introduce ip to scan" y
nmap -sn -Pn $y

elif [ $varname -eq 4 ]; then
echo "routing table"

elif [ $varname -eq 5 ]; then
traceroute $host

else
echo "Exiting..."

fi
