## 6.0 Python 实现去重
# list1 = [11,11,11,12,12,12,13]
# print(set(list1))

## 7.0 fun(*args, **args) 中参数的含义
## *args & **args 主要用于函数定义， 可以将不定数量的参数传递给一个函数，也就是说预先并不知道函数使用这会传递多少个参数，在这个长江下使用这两个关键字， * args 用来发送一个非键值对的可变数量的参数列表
## 给一个函数

# def demo (args_f,*argsv):
#     print(args_f)
#     for x in argsv:
#         print(x)
# demo(2)

## **args 允许你将不定长度的键值对，作为参数传递给一个函数， 如果你想要在以恶函数处理带名字的参数，那就应该使用**kwargs

# def demo(**args_v):
#     for k,v in args_v.items():
#         print(k,v)

# demo(name = "1", name1 = "2")

## 8.0 python2 & pyton3 中的range(100) 的区别
# print(list(range(1,10)))
# print(type(range(1,10)))

## 9.0 一句话解释什么样的语言呢鞥给用装饰器
## 函数可以作为参数传递的语言，可以使用装饰器

## 10. pyython 的数据类型 int/bool/str/list/tuple/dict

## 11. 简述面向对象中__new__ & __init__ 的区别
## _init__ 使初始化方法， 创建对象后， 就立刻被默认调用了， 可接受参数
# class Bikr:
#     def __init__(self,newWheelNum, newColor):
#         self.whellNUm = newWheelNum
#         self.color = newColor

#     def move(self):
#         print("runing the car")

# BM = Bikr(2, "red")
# print("the care {0}, {1}".format(BM.color,BM.whellNUm))

## __new__ 至少有一个参数cls, 代表当前类， 这个参数在实例化时有Python 解释器自动识别
## __new__ 必须要有返回值， 返回实例化出来的实例自己在实现__new__ 的时候， 注意可以return 父类（suple(当前类名, cls)）__new__ 出来的实例, 或者直接使object 的 —__new__ 出来的实例
## __init__ 有一个参数self， 就是这个__new__ 返回的实例, __init__ 在__new__的举出上完成其他的初始化的动作, __init__ 不需要返回值
## 如果用__new__ 创建当前类的实例, 会自动调用__init__ 函数， 通过return语句里卖弄调用的__new__ 函数的第一个参cls 拉保证是当前类实例，如果使其他类的类名， 南无实际创建返回的记忆是其他类的实例，
## 其实就不会调用当前类的__init__ 函数， 也不会调用其他类的__init__ 函数

# class A(object):
#     def __init__(self):
#         print("init",self)

#     def __new__(cls):
#         print("cls ID", (id(cls))
#         print(object.__new__(cls))

#         return object.__new__(cls)
# A()
# print("Claas A",id(A))

## 12. 简述with 方法打开处理文件帮我们做了什么
## with 方法帮我们实现了finally 中的 close

## 13. 列表[1,2,3,4,5], 请使用map() 函数输出[1,4,9,,16,15] 并且用列表推导式提取出大于10的数字， 输出[16,15]
# ls = [1,2,3,4,5]
# rs =[x for x in list(map(lambda x: x*x,ls)) if x >10] 
# print(rs)

## 14. python 中生成随机整数,随机小数, 和 0 ~1 之间小数的方法
## 随机整数  random.randint(a,b); 随机小数:numpy.random.randn(5);0 ~1 随机小数 random.random()

# import  random
# import numpy as np
# print(random.randint(10,20))
# print(np.random.randn(5))
# print(random.random())

##15. 'r' 表示原始字符串， 不转义特殊字符

