# 第16章 创建函数

## 基本的脚本函数

### 创建函数

```shell
function name {
  commands
}
```

或

```shell
name() {
  commands
}
```

使用函数

```shell
#!/bin/bash
#using a function in a script

function func1 {
	echo "this is a example of function"
}
count=1
while [ $count -le 3 ]
do
	func1
	count=$[ $count+1 ]
done

echo "end"
```

## 函数返回值

### 默认退出状态码

默认情况下，函数的退出码是函数中最后一条命令返回的退出状态码。

### 使用return命令

return命令允许指定一个整数值来定义函数的退出状态码。但需要注意的是：1. 函数一结束就取返回值 （在使用$?变量）2. 退出状态码必须在0~255之间。

### 使用函数输出

可以将函数的输出保存到shell变量中。

使用示例：

```shell
#!/bin/bash
#using the echo to return a value

function func2 {
	read -p "enter a value: " value
	echo $[ $value * 2 ]
}

result=`func2`
echo "the new value is $result"
```

## 在函数中使用变量

### 向函数传递参数

在脚本中指定函数时，必须将参数和函数放在同一行，就像这样：

```shell
func1 $value1 $value2
```

使用示例：

```shell
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
```

### 在函数中处理变量

- 全局变量。默认情况下，在脚本中定义的任何变量都是全局变量。在函数外定义的变量在函数内正常访问。
- 局部变量。函数内部使用的任何变量都可以被声明成局部变量，在声明变量的前面加上local关键字就可以了。

```shell
#!/bin/bash
# demonstrating a bad use of variables

function func4_1 {
	temp=$[ $value + 5 ]
	result=$[ $temp * 2]
}
temp=4
value=6
func4_1

echo "the result is $result"
if [ $temp -gt $value ]
then
	echo "temp is larger"
else
	echo "temp is smaller"
fi
```

这时候输出的结果是`temp is larger`。

这是需要在变量声明的前面加上local关键字就可以了：

`local temp=$[ $value + 5 ]`

## 数组变量和函数

### 向函数传数组参数

```shell
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
```

### 从函数返回数组

```shell
#!/bin/bash
# return an array value

function func6 {
	local originarray
	local newarray
	local elements
	local i
	originarray=(`echo "$@"`)
	newarray=(`echo "$@"`)
	elements=$[ $# - 1 ]
	for (( i=0; i<=$elements; i++ ))
	{
		newarray[$i]=$[ ${originarray[$i]} * 2 ]
	}
	echo ${newarray[*]}	
}

myarray=(1 2 3 4 5)
echo "the origin array is: ${myarray[*]}"
arg1=`echo ${myarray[*]}`
result=(`func6 $arg1`)
echo "the new array is: ${result[*]}"
```

## 函数递归

使用示例：计算阶乘

```shell
#!/bin/bash
# using recursion

function factorial {
	if [ $1 -eq 1 ]
	then
		echo 1
	else
		local temp=$[ $1 - 1 ]
		local result=`factorial $temp`
		echo $[ $result * $1 ]
	fi
}

read -p "enter value : " value
result=`factorial $value`
echo "the factorial of $value is: $result"
```

## 创建库

1. 新建一个库文件myfunc
2. 在shell脚本中使用`. ./myfunc`运行myfunc库文件

```shell
# my script functions

function addem {
	echo $[ $1 + $2 ]
}

function multem {
	echo $[ $1 * $2 ]
}

function divem {
	if [ $2 -ne 0 ]
	then
		echo $[ $1 / $2 ]
	else
		echo -1
	fi
}

#----------------------------------------------------
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
```

## 命令行上使用函数

### 命令行上创建函数

```shell
$ function divem { echo $[ $1 / $2 ]; }
$ divem 100 5
20
```

注意记得在每个命令后面加一个分号。

### 在.bashrc文件中定义函数

- 直接定义函数
- 读取函数文件