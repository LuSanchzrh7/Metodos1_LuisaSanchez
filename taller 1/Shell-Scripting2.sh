#!/bin/bash

function help(){
	echo "Debes ingresar TRES valores: la posición inicial, la velocidad inicial, y el tiempo total"
}

if ! [ ${#} -eq 3 ]; then
	help
	exit 1
else
	echo "Corriendo Programa..."
fi
