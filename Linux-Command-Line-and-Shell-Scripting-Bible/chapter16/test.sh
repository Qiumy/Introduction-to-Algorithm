#!/bin/bash
# using function defined in a library file

source ./myfuncs

value1=10
value2=5
result1=`addem $value1 $value2`
result2=`multem $value1 $value2`
result3=`divem $value1 $value2`

echo "the result of adding them is: $result1"
echo "the result of multiplying them is: $result2"
echo "the result of dividing them is: $result3"