import math

print('hello word')
print(math.exp(1))

import random

random.seed()
print ("使用默认种子生成随机数：", random.random())

random.seed(10)
print ("使用整数种子生成随机数：", random.random())

random.seed("hello",2)
print ("使用字符串种子生成随机数：", random.random())

random.seed(5)
num = 0
while num<5:
    print(random.random())
    num+=1
    
print(math.e)