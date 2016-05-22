#!/bin/bash
# extracting command line options and values

while [ -n "$1" ]
do
	case "$1" in
		-a) echo "found the -a options";;
		-b) param="$2"
			echo "found the -b option with parameter value $param"
			shift;;
		-c) echo "found the -c option";;
		--) shift
			break;;
		*) echo "$1 is not an option";;
	esac
	shift
done

