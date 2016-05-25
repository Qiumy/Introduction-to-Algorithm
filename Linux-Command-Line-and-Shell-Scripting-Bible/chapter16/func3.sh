#!bin/bash
# try to acess script parameters inside a function

function func3 {
	echo $[ $1 * $2 ]
}

if [ $# -eq 2 ]
then
	value=`func3 $1 $2`
	echo "the result is $value"
else
	echo "usage: func3 a b"
fi
