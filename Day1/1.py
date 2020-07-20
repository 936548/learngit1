## 一行代码实现 1 ~ 100 的 和
## import random
# sr = sum(range(1,101))
# sl = list(range(1,101))
# sf = type(range(1,101))
# print(sr)
# print(sl)
# print(sf)

## 如何再一个函数内部修改全局变量

# a = 5
# def testing_global():
#     global a
#     a = 4
# testing_global()
# print(a)

## 列出5个python 标准库
## OS: 提供了与操作系统相关联的函数； sys: 命令行参数； re: 正则匹配； math: 数学运算, datetime： 处理日期时间

## 字典如何删除合并两个字典： del & update methods
# dic1 = {"name":"Li", "age":12}
# dic2 = {"name":"Zheng", "age":21}

# del dic1["name"]
# print(dic1)
# dic2.update(dic1)
# print(dic2)


## GIL 
## GIL 是Python 的全局解释器。 同一进程中假如有多个线程运行，一个线程在运行Python程序的时候会霸占Python 解释器（加了一把锁即GIL）使该进程的其他线程无法运行， 等该进程完成之后其他线程才能运行，如果线程运行过程中遇到耗时操作， 则解释器
##  锁解开，使其他线程运行，所以在多线程中， 线程的运行仍然使有先后顺序的， 并不是同时运行