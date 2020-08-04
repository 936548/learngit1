## 101 求两个列表的交集 差集 并集
# a = [1,2,3,4]
# b = [4,3,5,6]

# rs1 = [i for i in a if i in b] ## 在a 中的 i 并且也在 b 中 就是交集
# rs2  = list(set(a).intersection(set(b))) 

# rs3 = list(set(a).union(set(b)))
# rs4 = list(set(b).difference(set(a))) # b 中有而a中没有的
# rs5 = list(set(a).difference(set(b))) # a中有而b中没有的

# print("交集", rs1)
# print("交集", rs2)

# print("并集",rs3)

# print("差集",rs4)
# print("差集",rs5)


## 102. 生成0-100 之间的随机数   random.random() 生成0-1 之际去哪的随机小数 在乘以 100
# import random
# rs1 = int(100 * random.random())
# rs2 = random.choice(range(0,101))
# rs3 = random.randint(1,100)

# print(rs1)
# print(rs2)
# print(rs3)

## 103. lambda 匿名函数的好处  精简代码 lambda 省去了定义函数 map 省去了写 FOR 循环过程 res = list(map(lambda x: "" if x ==" else x,a"))

## 104.0 常见的网络传输协议 UDP, TCP. FTE. heep, smtp

## 105.0 单双三引号的分别用法  单引号里面可以使用双引号 不用转义字符 单引号包含单引号的时候 需要转义 三引号可以书写多行

## 106.0 python 中 正则search 和match 的区别
# import re
# s = "小明年龄13岁 工资10000"

# rs3 = re.match("工资",s).group()  # 匹配以小明开头的字符串并且匹配 不叫group 是匹配不到的
# print(rs3)

# rs3 = re.match("小明",s).group()  匹配以小明开头的字符串并且匹配 不叫group 是匹配不到的
# print(rs3)

# rs1 = re.search(r"\d+?",s).group() # search 匹配到第一个匹配的数据
# print(rs1)

# rs2 = re.findall(r"\d+",s)  满足正则 全部匹配不用加group 
# print(rs2)





