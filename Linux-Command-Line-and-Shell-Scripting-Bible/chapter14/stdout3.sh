#!/bin/bash
#storing STDPPUT. then coming back to it

exec 3>&1
exec 1>test4out

echo "this should store in output file"
echo "along with this line"

exec 1>&3

echo "be back to normal"
