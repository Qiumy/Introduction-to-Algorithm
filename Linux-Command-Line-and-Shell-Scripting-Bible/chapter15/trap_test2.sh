#!/bin/bash
# removing a set trap

trap "echo byebye" EXIT

count=1
while [ $count -le 5 ]
do
	echo "loop #$count"
	sleep 2
	count=$[ $count + 1 ]
done
trap - EXIT
echo "i just removed the trap"
