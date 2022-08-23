#!/bin/bash
n=20
m=$(($n+1))
facto=1
function factorial(){
	local control=1
	while [ $m -gt $control ]
	do
		local mult=$control
		facto=$(($facto*$control))
		let control=$control+1
	done
}
factorial
echo "el factorial del numero $n es:$facto"
