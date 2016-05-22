#!/bin/bash
# extracting command line options and values with getopt

while getopts :ab:cd opt
do
	case "$opt" in
		a) echo "found the -a options";;
		b) echo "found the -b option with parameter value $OPTARG";;
		c) echo "found the -c option";;
		*) echo "unknown option: $opt";;
	esac
done

shift $[ $OPTIND - 1 ]

count=1
for param in "$@"
do
	echo "Parameter #$count: $param"
	count=$[ $count + 1 ]
done
