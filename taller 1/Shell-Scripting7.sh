#!/bin/bash
read -p "escriba el numero (n) al que se calculara su factorial: " n
m=$(($n+1)) 
facto=1
function factorial(){
	for i in $( seq 1 $n )
do
	facto=$(($facto*$i))
	if [ $i -le 20 ]; then
		echo $facto
	fi
done
}
factorial
echo "el factorial del numero $n es:$facto"

