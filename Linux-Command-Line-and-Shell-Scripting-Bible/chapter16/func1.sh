#!/bin/bash
#using a function in a script

function func1 {
	echo "this is a example of function"
}
count=1
while [ $count -le 3 ]
do
	func1
	count=$[ $count+1 ]
done

echo "end"
