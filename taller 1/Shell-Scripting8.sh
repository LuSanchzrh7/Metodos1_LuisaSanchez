#!/bin/bash

read -p "escriba el nombre del archivo con su debido indicador del tipo:" nombre

archivo=$nombre
j=0
for i in `cat ${archivo}`;
do
	array[j]=$i
	j=$(($j+1))
done
echo ${array[2]}
