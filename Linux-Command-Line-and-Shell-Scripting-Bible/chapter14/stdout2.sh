#!/bin/bash
# using an alternative file descript

exec 3>testout3

echo "this should display on the monitor"
echo "this should be store in the file" >&3
echo "this should be back on the monitor"
