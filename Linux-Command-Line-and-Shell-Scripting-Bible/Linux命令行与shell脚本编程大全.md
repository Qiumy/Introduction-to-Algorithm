# 第10章 构建基本脚本

## 重定向输入和输出

### 输出重定向

- 采用大于号（>）来完成将命令的输出发到一个文件中。如果输出文件已经存在，则会用新的文件数据覆盖已经存在的文件。

```shell
$ command > outputfile
```

- 使用双大于号（>>）可以用来追加数据。

```shell
command >> outputfile
```

### 输入重定向

- 使用小于号（<）将文件的内容重定向到命令。

```shell
$ command < inputfile
```

`wc`命令提供了对数据中文本的计数。默认情况下，会输出3个值：文本的行数、文本的词数、文本的字节数。

## 管道

发送某个命令的输出作为另一个命令的输入。

```shell
$ command1 | command2
```

## 执行数学运算

### expr

```shell
$ expr 1 + 5
$ expr 5 \* 2
```

在shell脚本中使用expr命令需要使用反引号`。

### 使用方括号

```shell
$ var1 = $[1+5]
$ var2 = $[$var1 * 2]
```

bash shell数学运算符只支持整数运算。

### 浮点解决方案

使用内建的bash计算器，通过`bc`命令访问bash计算器。bash计算器可以识别数字、变量、注释、表达式、编程语言、函数。

浮点运算由一个内建的scale的变量控制的。设定小数点后面的位数，默认值为0。

```shell
$ bc
scale = 4
```

- 在脚本中使用bc：可以使用反引号来运行bc命令并输出赋给一个变量，基本格式如下：

```shell
variable=`echo " scale=4: 3.44 / 5" | bc`
```

## 退出脚本

### 查看退出状态码

使用$?专属变量来保存上个执行的命令的退出状态码。按照惯例，一个成功结束的命令的退出状态码是0。

| 状态码   | 描述            |
| ----- | ------------- |
| 0     | 命令成功结束        |
| 1     | 通用未知错误        |
| 2     | 误用shell命令     |
| 126   | 命令不可执行        |
| 127   | 没找到命令         |
| 128   | 无效退出参数        |
| 128+x | Linux信号x的严重错误 |
| 130   | 命令通过ctrl+c终止  |
| 255   | 退出状态码越界       |

# 第11章 使用结构化命令

## 使用if-then语句

bash shell的if语句会运行if行定义的那个命令。如果该命令的退出状态码是0（该命令成功运行），位于then部分的命令就会执行。否则then部分的命令不会执行。

```shell
if command
then
	commands
fi
```

## if-then-else语句

```shell
if command
then
	commands
else
	commands
fi
```

## 嵌套if

```shell
if command1
then
	command set 1
elif command2
then
	command set 2
elif command3
then
	command set 3
fi
```

## test命令

如果test命令中列出的田间成立，test命令就会退出并返回退出状态码0；否则会退出并返回退出码1。

```shell
test condition
```

- 在if-then语句中的使用

```shell
if test condition
then
	commands
fi

if [ condition ]
then
	commands
fi
```



test命令可以判断三类条件：数值比较、字符串比较、文件比较。

### 数值比较

```shell
n1 -eq n2
n1 -ge n2
n1 -gt n2
n1 -le n2
n1 -lt n2
n1 -ne n2
```

### 字符串比较

```shell
str1 = str2
str1 != str2
str1 < str2
str1 > str2
-n str1   #检查str1的长度是否非0
-z str1   #检查str1的长度是否为0
```

- 使用大于小于符号必须转义，否则shell会把它们当做重定向符号而把字符串的值当做文件名

### 文件比较

```shell
-d file    #检查file是否存在并是一个目录
-e file    #检查file是否存在
-f file    #检查file是否存在并是一个文件
-r file    #检查file是否存在并可读
-s file    #检查是否存在并非空
-w file    #检查file是否存在并可写
-x file    #检查file是否存在并可执行
-O file    #检查file是否存在并属当前用户所有
-G file    #检查file是否存在并且默认组与当前用户相同
file1 -nt file2    #检查file1是否比file2新
file1 -ot file2    #检查file1是否比file2旧
```

## 复合条件测试

```shell
[ condition1 ] && [ condition2 ]
[ condition1 ] && [ condition2 ]
```

## if-then的高级特性

### 使用双圆括号

```shell
(( expression ))
```

术语expression可以是任意的数学复制或者比较表达式。

### 使用双方括号

```shell
[[ expression ]]
```

双方括号命令提供了针对字符串比较的高级特性。可以使用模式匹配。

```shell
if [[ $user == r* ]]
then
	echo "hello $user"
else
	echo "Sorry. I do not know you!"
fi
```

## case命令

```shell
case variable in
pattern1 | pattern2)
	commands1;;
pattern3)
	commands2;;
*)
	default commands;;
esac
```

# 第12章 更多的结构化命令

## for命令

```shell
for var in list
do
	commands
done
```

### 读取列表中复杂的值

- 使用转义字符（反斜线）来将单引号转义
- 使用双引号来定义用到单引号的值

### 从变量中读取列表

```shell
list="test1 test2 test3"
for word in $list:
do 
	echo "hello $word?"
done
```

### 从命令中读取值

```shell
file = "states"
for state in `cat $file`
do
	echo "visit $state"
done
```

### 更改字段分隔符

默认情况下，bash shell会将下列字符当作字段分隔符：空格、制表符、换行符。

```shell
file = "states"
IFS=$'\n'
for state in `cat $file`
do
	echo "visit $state"
done
```

### 通过通配符读取目录

```shell
for file in /home/test/*
do
	echo "this is file $file"
done
```

## c语言风格的for

```shell
for (( i=1; i<=10; i++ ))
do
	echo "then next number is $i"
done
```

## while命令

```shell
while test command
do
	commands
done
```

### 使用多个测试命令

```shell
var1 = 10
while echo $var1
	[ $var1 -ge 0]
do
	echo "this is inside the loop"
	var1$[ $var1 -1 ]
done
```

## until命令

```shell
until [ $var1 -eq 0 ]
do 
	echo $var1
	var1=$[ $var1 -25 ]
done
```

- 嵌套循环

## 控制循环

- break命令
- continue命令

## 处理循环的输出

在done命令之后可以添加一个处理命令，要么管接要么重定向循环的输出。

```shell
...
done > ouput.txt

...
done | sort
```

# 第13章 处理用户输入

## 命令行参数

\$0是程序名，\$1是第一个参数，\$2是第二个参数，以此类推，直到第9个参数\$9。可以使用test命令里使用了-n参数来检查命令行参数是否有数据。

## 特殊参数变量

\$#特殊变量含有脚本运行时就有的命令行参数的个数。

变量${!#}代表了最后一个命令行参数变量。

### 抓取所有的数据

\$*和\$@变量提供了对所有参数的快速访问。这两个都能够在单个变量中存储所有的命令行参数。

\$*变量会把命令行上提供的所有参数当做单个单词保存。

\$@变量会将命令行上提供的所有参数当做同一个字符串中的多个独立的单词。它允许你遍历所有的值，将提供的每个参数分割开来。

```shell
count=1
for param in "$*"
do 
	echo "\$* Parameter #$count = $param"
done

count=1
for param in "$@"
do
	echo "\$@ Parameter #$count = $param"
done
```

## 移动变量

shift会根据它们的相对位置来移动命令行参数。

## 处理选项

### 查找选项

- 处理简单选项

```shell
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
```

- 分离参数和选项

```shell
#!bin/bash
# extracting command line options as parameters

while [ -n "$1" ]
do
	case "$1" in
		-a) echo "found the -a option";;
		-b) echo "found the -b option";;
		--) shift
			break;;
		*) echo "$1 is not an option";;
	esac
	shift
done	
```

- 处理带值的选项

```shell
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
```

### 使用getopt命令

```shell
#getopt optstring options parameters
$getopt ab:cd -a -b test1 -cd test2 test3
# -a -b test1 -c -d -- test2 test3
```

```shell
#!/bin/bash
# extracting command line options and values with getopt

set -- `getopt -q ab:c "$@"`

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

count=1
for param in "$@"
do
	echo "Parameter #$count: $param"
	count=$[ $count + 1 ]
done
```

### 使用更高级的getopts

```shell
getopts optstring variable
```

getopts命令会使用到两个环境变量。如果选项需要跟一个参数值，OPTARG环境变量会保存这个值。OPTIND环境变量保存了参数列表中getopts正在处理的参数位置。

## 将选项标准化

例如在使用read命令的时候，使用-p选项允许世界在read命令行指定提示符；使用-t选项指定read命令等待输入的秒数；使用-s选项组织奖传给read命令的数据显示在显示器上。

显示例子说明将文件中的数据传给read命令。将文件运行cat命令后的输入通过管道直接传给含有read命令的while命令。

```shell
#!/bin/bash
# reading data from a file

count=1
cat test | while read line
do
	echo "Line $count: $line"
	count=$[ $count + 1 ]
done
echo "fininshed processing the file"
```

