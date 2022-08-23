#!/bim/bash
n=20
r=3

function factorial(){
	facto=1
	local m=$(($n+1))
        local control=1
        while [ $m -gt $control ]
        do
                local mult=$control
                facto=$(($facto*$control))
                let control=$control+1
        done
}

factorial
numer=$facto
n=$(($n-$r))
factorial
divi=$facto
resultado=$(($numer/$facto))
echo $resultado

echo "la complejidad del algoritmo es O(n)"
