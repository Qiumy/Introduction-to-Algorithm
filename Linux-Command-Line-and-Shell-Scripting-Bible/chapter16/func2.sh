#!/bin/bash
#using the echo to return a value

function func2 {
	read -p "enter a value: " value
	echo $[ $value * 2 ]
}

result=`func2`
echo "the new value is $result"
