#!/bin/bash
# return an array value

function func6 {
	local originarray
	local newarray
	local elements
	local i
	originarray=(`echo "$@"`)
	newarray=(`echo "$@"`)
	elements=$[ $# - 1 ]
	for (( i=0; i<=$elements; i++ ))
	{
		newarray[$i]=$[ ${originarray[$i]} * 2 ]
	}
	echo ${newarray[*]}	
}

myarray=(1 2 3 4 5)
echo "the origin array is: ${myarray[*]}"
arg1=`echo ${myarray[*]}`
result=(`func6 $arg1`)
echo "the new array is: ${result[*]}"
