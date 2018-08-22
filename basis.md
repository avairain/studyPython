# python3
## print 
    基础打印 用来查看一个对象的方法 print('Hello world')
## type()
    查看变量所指的对象的类型 type(1)
## isinstance()
    待续
## 数据类型
  * Number
  * String
  * List
  * Tuple
  * Set
  * Dictionary
### Number 数字
    * int(整数), float(小数), bool(布尔值: true | false), complex(复数)
    * 数字支持加(1 + 1)减(1 - 1)乘(1 * 1)除(1 / 1 >> 1.0), 以及取余(5 % 3 >> 2), 乘方(2**3 >> 2 * 2 * 2 >> 8) 和 整除(9 // 2 >> 4)
    * del 语句 删除一个或者多个 ```del a,b``` ```del list[0]```
    * Number相关的方法

函数 | 描述
- | :-:
abs | 绝对值
ceil | 向上取整 math.ceil
exp | e的n次方 math.exp
fabs | 绝对值(带小数) math.fabs
fabs | 绝对值(带小数) math.fabs
floor | 向下取整 math.floor
log | math.log(10,3) 3的多少次方是10
log10 | math.log10(3) 10的多少次方是3
max | 最大值 max(1,2,3) max([1,2,3])
min | 最小值 min(1,2,3) min([1,2,3])
modf | 拆分整数和小数 math.modf(1.1)
pow | 乘方 math.pow(a,b) a的b次方
round | 四舍五入 round(1.1)
round | 四舍五入 round(1.1)
sqrt | 平方根 math.sqrt(100)
随机数 | --
random |  ```n >= 0 and n< 1``` random.random
choice | random.choice(range(10)) 0-9的整数
randrange | random.randrange([start,] stop [,step]) 不包含stop random.randrange(1, 100, 2) 1 - 100 的奇数
seed | 使多次生成的随机数相同 random.seed
shuffle | random.shuffle 随机排列序列
uniform | 随机生成一个数 random.uniform(5, 10) 5-10 之间
三角函数 | --
sin | 正弦 math.sin
cos | 余弦 math.cos
tan | 正切 math.tan
asin | 反正弦 math.asin
acos | 反余弦 math.acos
atan | 反正切 math.atan
atan2 | X 及 Y 坐标值的反正切值 math.atan2
hypot | 欧几里德范数 sqrt(x*x + y*y)
degrees | 弧度 ==> 角度
radians | 角度 ==> 弧度

  * 数学常量

值 | 描述
- | :-:
pi | math.pi 圆周率
e | math.e 自然常数
** math 需要引入 ``` import math ```
** random 需要引入 ``` import random ```
### String 字符串
    * 用单引号(')或者双引号(")包起来的序列
    * 字符串的截取 获得一个新的序列
    ```python
    str[start:end]
    ```
    * example:
    ```python
      str = "我是字符串"
      print(str[0]) # 我
      print(str[0:1]) # 我
      print(str[2:4]) # 字符
      print(str[0:-1]) # 我是字符
      print(str * 2) # 我是字符串我是字符串
      print(str + 2) # 我是字符串2
      str[0] = 'wo' # error  不能修改
    ```
    * 内置对象

函数 | 描述
- | :-:
len | 字符串的长度
capitalize | 第一个字符变成大写
center | str.center(40,'*') 将 `str`左右填充`'*'` 到长度为 40 默认 空格
rjust | 类似center 不过是只左填充
zfill | 类似center 不过是只左填充, 且填充 `'0'`
count | 某个字符出现的次数 str.count('a', start, end) `str` 中 `'a'`在start到end之间(不含end)出现的次数
encode | 译成编码对应的编码字符串 str.encode('UTF-8','strict')
decode | 译成编码字符串对应的编码 code.decode('UTF-8','strict')
endswith | 字符是不是结尾 str.endswith(s, start, end) `str`中 `s`在start到end之间是不是结尾  >> True || False
startswith | 类似 endswith 不过是判断开始
expandtabs | 把tab缩进替换成空格 默认 8
find | 查询索引 str.find(s, start, end)  找到返回 索引 未找到返回 -1
rfind | 类似find 不过是从右开始
index | 字符包含在内  找到返回 索引 未找到 抛异常
rindex | 类似index 不过是从右开始
isalnum | 判断字符串不为空, 且只存在字母或者数字
isalpha | 判断字符串不为空, 且只存在字母
isdigit | 判断字符串不为空, 且存在数字
islower | 判断字符串存在字母, 且都为小写
isupper | 判断字符串存在字母, 且都为大写
isnumeric | 判断字符串只存在数字
isspace | 判断字符串只存在空白
istitle | 判断字符串每个单词的首字母都是大写
title | 所有单词都是以大写开始,其余字母均为小写
join | str.join(list) 将 ``list``` 中的元素 以`str`拼接
lower | 转成小写
upper | 转成大写
swapcase | 大写转小写,小写转大写
strip | 去掉左右的指定字符 默认空格
lstrip | 去掉左边的指定字符 默认空格
rstrip | 去掉右边的指定字符 默认空格
maketrans | str.maketrans('ab','12') 将`str`中的 `a` 替换成 `1`,`b` 替换成 `2`
max | max(str) `str`中最大的字母
min | min(str) `str`中最小的字母
replace | str.replace('ab', 'AB', 3) 将`str`中 `'ab'` 替换成`'AB'` 最多替换3次
split | 按指定字符截取字符串 split('s', 1) 以`'s'`截取, 最多截取 1 次
isdecima | 判断是否只包含十进制字符

### List 列表
    * 在``` [] ```之间用```,```隔开的元素的序列
    * 列表的截取 获得一个新的序列
    ```python
    list[start:end]
    ```
    类似于String的截取, 但是 ```list```可以修改原对象的元素
    * example: 
    ```python
      list = ['我','是','LIST','!']
      list1 = ['!']
      list[2] = 'list'
      print(list) # ['我','是','list','!']
      print(list + list1) # ['我','是','list','!','!']
    ```

函数 | 描述
- | :-:
append | 后面添加一个
pop | 删除索引对应的值 默认 -1
remove | 删除匹配的第一个元素
len | 列表的长度
list | 元组转换为列表
count | 某元素出现次数
extend | 将元组追加到列表后面
index | 查找某个元素的索引
insert | list.insert(1,'a') 在`list`的第二个元素前插入一个 `'a'`
reverse | 翻转 列表
sort | 排序 默认是从小到大 list.sort(key = None, reverse = False) 从大到小 key 可以是是函数
clear | 清空
copy | 复制

### Tuple 元组
    * 在``` () ```之间用```,```隔开的元素的序列(类似于列表, 但元素不能修改)
    * 元组的截取 获得一个新的序列
    ```python
    tuple[start:end]
    ```
    * example:
    ```python
      tup1 = ()    # 空元组
      tup2 = (20,) # 一个元素，需要在元素后添加逗号
      tuple = ([1],[2]) # 内部的列表不能修改 单列表里面的元素可以修改
    ```
    * tuple(list)
    将列表转换为元组
### Set 集合
    * 在``` {} ```之间用```,```隔开的无序不重复元素的序列
    * 创建
    ```python
      parame = { value01, value02 }
      set(value)
    ```
    ``` 创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典 ```
    * example:
    ```python
      print(set(1,1,1,1)) # {1} 重复的元素被自动去掉
    ```
    * add()
      - 添加一项
    * update(obj or list or tuple,[])
      - 添加多个
    * remove(key)
      - 删除一个 元素不存在会抛异常
    * discard(key)
      - 删除一个 元素不存在不会抛异常
    * pop()
      - 随机删除
    * len()
      - 计算集合元素个数
      
### Dictionary 字典
    * 无序的集合, 通过键来存取的
    * example: 
    ```python
      dict = {}
      dict[1] = 'D'
      dict1 = {'d': 'D','i': 'I', 'c': 'C', 't': 'T'}
      print(dict1.keys()) # dict_keys(['d', 'i', 'c', 't'])
      print(dict1.values()) # dict_keys(['D', 'I', 'C', 'T'])
    ```
    + 创建字典
      - dict()
      ```python
        print(dict([('1', 1), ('2', 2), ('3', 3)])) # {'1': 1, '2': 2, '3': 3}
        print(dict({x: x**2 for x in (2, 4, 6)})) # {2: 4, 4: 16, 6: 36}
        print(dict(a = 1, b = 2, c = 3)) # {'a': 1, 'b': 2, 'c': 3} 这个方式 的 key 不能为 数字
      ```
    * clear()
      - 清空字典
    * copy()
      - 浅复制
    * fromkeys(list[,val])
      - list 里面的每一个值映射到 字典中 值为val
    * get(key,'default')
      - 查找 字典 key 对应的值  默认返回 `'default'` 不会改变原字典
    * setdefault(key,'default')
      - 查找 字典 key 对应的值 返回 不存在就射为 `'default'` 改变原字典
    * items()
      - 以列表返回可遍历的(键, 值) 元组数组
    * keys()
      - 可遍历的键的列表
    * values()
      - 可遍历的值的列表
    * pop(key)
      - 删除对应的键值对
    * popitem()
      - 通常为删除最后一个键值对
    * update(dict)
      - 将dict内的键值 添加到 原字典
    * 字典是一种映射类型，字典用"{ }"标识，它是一个无序的键(key) : 值(value)对集合
    * ``` 键(key)必须使用不可变类型 在同一个字典中，键(key)必须是唯一的 ```
## 数据类型转化

函数 | 描述 | 列子 | 结果
- | :-: | -: | -: | -:
int() | 转化成整数 | int('1') | 1
float() | 转化成浮点数 (小数) | float('1') | 1.0
complex() | 转化成复数 | complex('1', 1) | 1 + j
str() | 转化成字符串 | str(123) | '123'
repr() | 转化成字符串 | repr(123) | '123'
eval() | 用来计算在字符串中的有效Python表达式,并返回一个对象 | eval('1 + 1') | 2
tuple() | 序列转化成元组 | tuple([1]) | (1,)
list() | 序列转化成列表 | list([1]) | [1]
set() | 序列转化成Set集合 | set([1]) | {1}
dict() | 转化成字典 | dict({x: x**2 for x in (2, 4, 6)}) | {2: 4, 4: 16, 6: 36}
frozenset() | 转化成字典 | frozenset({x: x**2 for x in (2, 4, 6)}) | {2, 4, 6}

  * 注意输入的格式

## 注释 不解析的内容
  * 单行 ``` # 这是注释 ```
  * 多行 
  ```python
  '''
    这
    是
    注
    释
  '''
  """
    这
    也
    是
    注
    释
  """

  ```
  * **三引号可以定义一个跨行的字符串
## 运算符
  * ```+ - * / ** // ```
  * 比较运算符 返回bool值

运算符 | 描述
- | :-:
== | 比较对象是否相等
!- | 比较对象是否不相等
> | 大于
< | 小于
>= | 大于等于
<= | 小于等于

  * 赋值运算符

运算符 | 描述
- | :-:
= | 等于
+= | `a +=b >> a = a + b`
-= | `a -=b >> a = a - b`
*= | `a *=b >> a = a * b`
/= | `a /=b >> a = a / b`
%= | `a %=b >> a = a % b`
**= | `a **=b >> a = a ** b`
//= | `a //=b >> a = a // b`

  * 逻辑运算符

运算符 | 描述
- | :-: 
and | 10 and 20 >> 20
or | 10 or 20 >> 10
not | not True >> False

  * 成员运算符

运算符 | 描述
- | :-: 
in | 在指定的序列中找到值返回 True
not in | 在指定的序列中找到值返回 False

  * 身份运算符

运算符 | 描述
- | :-:
is | 判断两个标识符是不是引用自一个对象
not is | 判断两个标识符是不是引用自不同对象
  * 运算符优先级
    - `**` > ```~ + -'''正负'''``` > `* / % //` > ```+ - '''加减'''``` > `<= < >=` > `== !=` > `= %= /= //= -= += *= **=` > `is is not` > `in not in` > `and or not`