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

