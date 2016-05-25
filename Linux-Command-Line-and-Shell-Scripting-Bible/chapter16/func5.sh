#!/bin/bash
# array variable to function test

function func5 {
	local newarray
	newarray=(`echo "$@"`)
	echo "the new array value is ${newarray[*]}"
}

myarray=(1 2 3 4 5)
echo "the original array is ${myarray[*]}"
func5 ${myarray[*]}
