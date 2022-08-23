#!/bin/bash

function crear_dir(){
	mkdir data
}

DIRECTORY="data"

if [ -d "$DIRECTORY" ]; then
        echo "si"
else
        echo "no"
        crear_dir
fi
