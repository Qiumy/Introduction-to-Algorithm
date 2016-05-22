#!bin/bash
# extracting command line options as parameters

while [ -n "$1" ]
do
	case "$1" in
		-a) echo "found the -a option";;
		-b) echo "found the -b option";;
		*) echo "$1 is not an option";;
	esac
	shift
done	
