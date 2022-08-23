#!/bin/bash

pass=0

function checkvalue(){
	case "${N}" in 
	  1)
		  pass=$N
		  ;;
	  *)
		  pass=0
		  ;;
  esac
}

while [ $pass -ne 1 ]
do
	read N
	checkvalue
done
