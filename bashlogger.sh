#!/bin/bash

#datenow=$(date +"%Y-%m-%d %H:%M:%S") duas formas diferentes de fazer o mesmo, nota nos espaços
datenow= date "+%Y-%m-%d | %H:%M:%S"

#aqui se tiver um espaço entre = e $ nao funciona
username=$USER

#tem de ser parentesis retos senao nao funciona
echo "[$datenow]  User: $username"
#echo "$USER" outra forma de fzer o mesmo
echo "Log entry: Script executed correctly"
echo "===========================================================" 



