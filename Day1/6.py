## 51.0 正则表达式匹配url='https://sycm.taobao.com/bda/tradinganaly/overview/get_summary.json?dateRange=2018-03-20%7C2018-03-20&dateType=recent1&device=1&token=ff25b109b&_=1521595613462'

# import re
# url='https://sycm.taobao.com/bda/tradinganaly/overview/get_summary.json?dateRange=2018-03-20%7C2018-03-20&dateType=recent1&device=1&token=ff25b109b&_=1521595613462'
# res = re.findall(r'dateRange=(.*?)%7C(.*?)&',url)
# print(res)

## 52.0 list=[2,3,5,4,9,6]，从小到大排序，不许用sort，输出[2,3,4,5,6,9]
# ls = [2,3,5,4,9,6]
# new_ls= []

# def get_main(ls):
#     a = min(ls)
#     ls.remove(a)

#     new_ls.append(a)

#     if len(ls) >0:
#         get_main(ls)
#     return new_ls

# new_ls = get_main(ls)
# print(new_ls)

## 53.0 写一个单例模式  创建对象时 __new__ 方法执行 并且必须return 返回实例出来的对象 cls_instance 是否存在 不存在的话九九创建新对象 存在的话就返回该对象 保证只有一个实例对象存在 打印ID如果存在相同的值 说明对象就是同一个

# class Singleton(object):
#     __instance = None
#     def __new__(cls, age,name):
#         if not cls.__instance:
#             cls.__instance = object.__new__(cls)
#         return cls.__instance

# a = Singleton(15,"a")
# b = Singleton(14,"b")

# print(id(a))
# print(id(b))

## 54.0  保留两位小数  题目本身只有a="%.03f"%1.3335,让计算a的结果，为了扩充保留小数的思路，提供round方法（数值，保留位数）

# a=  "%.03f" % 1.335
# print(a, type(a))

# b  = round(float(a),2)
# c  = round(float(a),1)

# print(a)
# print(b)

## 55.0  3 中不同的方法打印结果  fn("one",1）直接将键值对传给字典；

# fn("two",2)因为字典在内存中是可变数据类型，所以指向同一个地址，传了新的额参数后，会相当于给字典增加键值对；

# fn("three",3,{})因为传了一个新字典，所以不再是原先默认参数的字典。

# def fn(k,v, dic ={}):
#     dic[k] =v
#     print(dic)

# fn("a",1)
# fn("b",2)
# fn("c",3,{})

## 56.0  200 OK 请求正常处理完毕204 No Content 请求成功处理，没有实体的主体返回 206 Partial Content GET范围请求已成功处理301 Moved Permanently 永久重定向，资源已永久分配新URI302 Found 临时重定向，资源已临时分配新URI303 See Other 
## 临时重定向，期望使用GET定向获取304 Not Modified 发送的附带条件请求未满足307 Temporary Redirect 临时重定向，POST不会变成GET400 Bad Request 请求报文语法错误或参数错误401 Unauthorized 需要通过HTTP认证，或认证失败403 Forbidden 
## 请求资源被拒绝404 Not Found 无法找到请求资源（服务器无理由拒绝）500 Internal Server Error 服务器故障或Web应用故障503 Service Unavailable 服务器超负载或停机维护

## 57.0 分别从前端后端web数据库阐述项目的性能优化  前端优化：

# 1、减少http请求、例如制作精灵图。
# 2、html和CSS放在页面上部，javascript放在页面下面，因为js加载比HTML和Css加载慢，所以要优先加载html和css,以防页面显示不全，性能差，也影响用户体验差。

# 后端优化
# 1、缓存存储读写次数高，变化少的数据，比如网站首页的信息、商品的信息等。应用程序读取数据时，一般是先从缓存中读取，如果读取不到或数据已失效，再访问磁盘数据库，并将数据再次写入缓存
# 2、异步方式，如果有耗时操作，可以采用异步，比如celery。
# 3、代码优化，避免循环和判断次数太多，如果多个if else判断，优先判断最有可能先发生的情况。

# 数据库优化
# 1、如有条件，数据可以存放于redis，读取速度快
# 2、建立索引、外键等。

## 58.0 使用pop和del删除字典中的"name"字段，dic={"name":"zs","age":18}

# dic = {"name":"zs","age":18}
# dic.pop("name")
# print(dic)

# dic1 = {"name":"zs","age":18}
# del dic1["name"]
# print(dic1)

## 59.0 列出常见MYSQL数据存储引擎 
# InnoDB：支持事务处理，支持外键，支持崩溃修复能力和并发控制。如果需要对事务的完整性要求比较高（比如银行），要求实现并发控制（比如售票），那选择InnoDB有很大的优势。如果需要频繁的更新、删除操作的数据库，也可以选择InnoDB，因为支持事务的提交（commit）和回滚（rollback）。 
# MyISAM：插入数据快，空间和内存使用比较低。如果表主要是用于插入新记录和读出记录，那么选择MyISAM能实现处理高效率。如果应用的完整性、并发性要求比 较低，也可以使用
# MEMORY：所有的数据都在内存中，数据的处理速度快，但是安全性不高。如果需要很快的读写速度，对数据的安全性要求较低，可以选择MEMOEY。它对表的大小有要求，不能建立太大的表。所以，这类数据库只使用在相对较小的数据库表。

## 60.0 计算代码运行结果，zip函数历史文章已经说了，得出[("a",1),("b",2)，("c",3), ("d",4), ("e",5)]

# A = zip(("a","b", "c", "d", "e"),(1,2,3,4,5))
# A0 = dict(A)
# A1 = range(10)
# A2 = [i for i in A1 if i in A0]
# A3 = [A0[s] for s in A0]
# print("A0",A0)
# print(list(zip(("a","b", "c", "d", "e"),(1,2,3,4,5))))
# print(A2)
# print(A3)

# S = dict([("NAME","1"), ["AGE",12]])
# print(S)
