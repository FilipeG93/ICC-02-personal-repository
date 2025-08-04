#!/bin/bash

{
#datenow=$(date +"%Y-%m-%d %H:%M:%S") duas formas diferentes de fazer o mesmo, nota nos espaços
datenow= date "+%Y-%m-%d | %H:%M:%S"

#aqui se tiver um espaço entre = e $ nao funciona
#username=$USER

#tem de ser parentesis retos senao nao funciona
echo "$datenow"
#echo "[$datenow]  User: $username" na mesma linha outra forma de fazer o mesmo
echo "User: $USER"


echo "difference between > and >> :
> writes text into a file deleting everything that was previously there
>> appends text to a file without overwriting what was previously there"

echo "Log entry: Script executed successfully"
echo "===========================================================" 
} >> user_activity.log
 



