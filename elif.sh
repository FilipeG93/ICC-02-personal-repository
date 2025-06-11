#!/bin/bash

#para fazer um maior que e menor que temos de usar && com dois parenteses diferntes cada condiçao num so

n=16

if [ $n -le 5 ]; then
echo "menor que cinco"

elif [ $n -le 10 ]; then
echo "maior que cinco e menor que dez"

elif [ $n -le 15 ]; then
echo "maior que dez e menor que quinze"

else
echo "maior que quinze"

fi


echo "versao 2"

n=6

if [ $n -gt 5 ] && [ $n -lt 10 ]; then
echo "esta entre 5 e 10"

else
echo "esta acima de 10"

fi

