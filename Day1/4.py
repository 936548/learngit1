## 31.0 合并两个列表 extend 可以将一个集合中的元素依次添加到另外一个列表中， 区别于appeand 整天添加

# s1 = [1,2,3,4]
# s2 = [5,6,7,8]
# s1.extend(s2)
# print(s1)
# s1.append(s2)
# print(s1)

## 32.0 python & linux 删除文件  python os.remove linux rm

## 33.0 log 日志中， 我们需要时间戳记录error, waring 发生的事件， 请用datatime 模块打印当前的时间戳 “20202-7-20 11：08：09” ,顺百年打印星期的时间
# import datetime
# a = str(datetime.datetime.now().strftime("%Y-%m-%d %H: %M: %S")) + "    week" + str(datetime.datetime.now().isoweekday())
# print(a)

## 34.0 数据库优化方法 外键 索引 联合查询 选定特定字符

## 35.0 举例 任意一种统计图 pychart matplotlib

## 36.0 写一段自定义异常用raise 抛出异常
# def fn():
#     try:
#         for i in range(5):
#             print(i)
#             if i >= 2:
#                 raise Exception("error")
#     except Exception as ret:
#         print(ret)

# fn()

## 37.0 正则表达式中 （.*） 和 （.*?） 的区别
##（.*） 是贪婪模式, 会尽可能多的进型匹配： （.*?） 非贪婪模式，在满足正则表达式的同时尽可能少的进型匹配

# import re
# s = "<a>123</a><a>456</a>"
# rs1 = re.findall("<a>(.*)</a>",s)
# rs2 = re.findall("<a>(.*?)</a>",s)
# print(rs1)
# print(rs2)

## 38.0 简述Diango 的 orm  ORM = Object -Relation Mappping = 对象-关系映射 实现了数据模型和数据库的解耦通过简单的配置快就可以轻松的更换数据库 而不需要修改代码 只需要面向对象编程 orm 操作
## 本质上会根据对接的数据可引擎 翻译成对应的sql 语句 所有使用Diango开发的仙姑不需要关心程序地城使用的是Mysql oracle splite 如果是数据库迁移 只需要更换Diangon 的数据库引擎就可以


## 39.0 用列表推导式展开列表 [[1,2],[3,4],[5,6]] 运行过程 for i in a 则每个 i  = [1,2] ,[3,4],[5,6] for j in i, 则 j = 1，2，3，4，5，6
# a = [[1,2],[3,4],[5,6]]
# rs = [j for i in a for j in i ]
# print(rs)
## 或者将列表转换成numpy 矩阵 通过numpy 的flatten() 方法

# import numpy as np
# a = [[1,2],[3,4],[5,6]]
# print(np.array(a))
# print(type(np.array(a)))
# print(np.array(a).flatten())
# print(type(np.array(a).flatten()))
# print(np.array(a).flatten().tolist())

## 40.0 x = "abc", y = "def", z = ["d", "e", "f"] 分别求出x.join(y), x.join(z) 的结果
## join() 括号里面的是可迭代对象 x 插入 可迭代对象中间， 形成字符串 结果一致
# y = "def"
# z = ["d", "e", "f"]
# print(" ".join(y))




