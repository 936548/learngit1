## 41.0 举例说明 Try except else finally 的相关意义 TrY\Except\Else 没有捕获到异常，执行else 语句. Try/Except/Finally  不管是否捕获到异常， 都执行Finally 与举报

## 42.0  Python 中交换两个数值  
## 啊，b = 3,4  A,B = B,A

## 43.0 Zip() 的用法
## zip() 函数在运算时，会以一个或者多个序列(可迭代对象) 作为参数,返回一个元组的列表, 同时将这些序列中并排的元素配对；zip() 参数可以接受任何类型的序列, 同时也可以有两个以上的参数; 当传入的参数长度不同时
## zip 能够自动以最短序列长度作为基准进型截取, 获得元组

# a = [1,2]
# b = [3,4,2]
# print([i for i in zip(a,b)])

# a = (1,2)
# b = (3,4,2)
# print([i for i in zip(a,b)])

# a = "qw"
# b = "asd"
# print( [i for i in zip(a,b)])

## 44.0 a = "张明98分" 用 re.sub 将98 替换为 100

# import re
# a = "张明98分"
# res = re.sub(r"\d+", "100",a)
# print(res)


## 45.0 写5条常用的sql 语句
## show databases show tables desc 表名 select * from 表明 update studetns et gender =0, hometown = "beijng" where id =5

## 46.0 a = "hello" 和 b = "你好" 编码成bytes类型
# a = "hello"
# b = "你好" 
# print(a.encode(), b.encode())

## 47.0 [1,2,3] + [4,5,6]
# A = [1,2,3] 
# B = [4,5,6]
# C1 =A.extend(B)
# C2 = A.append(B)

# print(A+B)
# print(C1)
# print(C2)

## 48.0 提高Python 运行效率的方法
## 1. 使用生成器节约内存 2. 循环代码优化,避免重复代码 3. 核心模块使用Cython,Pypy等 4. 多进程多次线程协程的使用 5. 多个if/else 的判断把最有可能先发生的条件放在最前面减少程序判断的次数

##49.0 简述mysql和redis的区别
## redis 内存型非关系数据库 数据保存在内存中 速度快
## mysql 关系型数据库 数据保存在磁盘中 检索的时候 会有一定的 IO 操作 访问速度比较慢

## 50.0 遇到debug 应该怎样处理
## 1. 细节上的错误 可以通过print() 打印 2. 涉及到第三方框架查看文档 3. 


