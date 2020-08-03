## 61.0 简述同源策略  需要同时满足 协议 域名 端口相同  

## 62.0 简述 cookie 和 session 的区别  
## 12. session 在服务端 cookie 是在客户端 浏览器
## session 的运行依赖 session is, 而session id  是存在 cookie 中的； 也就是说如果浏览器禁止使用 cookie 同时 session 也会失效 存储 session 的时候 键与 cookie 中 的sessionid 相同
# # 值是开发人员设置的键值对信息 进行了 base64 编码 过期由 开发人员设置
# # cookie 的安全性比session 差

## 63.  简述多线程和多进程的区别和联系
## 进程 操作系统是进型资源分配和调度的基本单位,多个进程之间相互独立 稳定性好 如果一个进程崩溃 不会影响其他进程 但是进程消耗资源大 开启的进程数量有限制
## 线程 cpu 进行资源分配和调度的基本单位 线程是进程的一部分 是比进程更小的能独立运行的基本单位 一个进程下的多个线程可以共享该进程的所有资源 如果是IO操作密集 可以用多线程进型运行 缺点是如果有一个线程崩溃
## 会造成进程的崩溃

## 64.0 简述any() all() 方法
## any() 只要迭代器中有一个元素为真就是真 all() 迭代器中的所有元素为真才是真
## Pyyhon 中为假的元素 0，空字符串/列表/字典/元组/None/False

## 65.0  IOError 输入输出异常、AttributeError 试图访问一个对象没有的属性、ImportError、 无法引入模块或包，基本是路劲问题IndentationError 语法错误代码没有正确的堆砌、IndexError下标索引超出序列边界、KeyError 访问字典不存在的键、SyntaxError、逻辑语法错误 不能执行NameError 使用一个还未赋予对象的变量分别代表什么异常

## 66.0 copy deepcopy 的区别
## 复制不可变数据类型 copy & deepcopy 都是同一个地址当浅复制的值是不可变对象  数值 字符串 元组 对象的ID 值与吉安府治原来的值相同
## 复制可变对象 列表和字典 复制的对象中无复杂子对象 原来值的改变不会影响浅复制的值 同时浅复制的值爱百年也不胡影响原来的值 原来的值的ID 与 浅复制原来的值不同
## 制的对象中有复杂子对象 eg 列表中一子元素是一个列表 改变原来值中的复炸子对象的值会影响浅复制的值
## deepcopy 完全复制独立 包裹内容列表和字典

## 67.0 魔术方法 __init__； 对象初始化  __new__ 创建对象时候执行的方法 单例模式会用到  __str__ 当使用print 输出对象的时候 只要自己定义了 __str__(self）就可以打印出return 返回的数据 __del__ 删除对象执行的方法

## 68.0 C:\Users\ry-wu.junya\Desktop>python 1.py 22 33命令行启动程序并传参，print(sys.argv)会输出什么数据？ [1.py 22,33]

## 69.0 请将[i for i in range(3)]改成生成器 生成器是特殊的迭代器：1、列表表达式的【】改为（）即可变成生成器 2、函数在返回值得时候出现yield就变成生成器，而不是函数了

##70、a = "  hehheh  ",去除收尾空格 a.strip()

## 举例sort和sorted对列表排序，list=[0,-1,3,-10,5,9]

# list=[0,-1,3,-10,5,9]
# res = list.sort(reverse=False) list.sort 是在list 的基础上进型修改 无返回值
# print(res)

# list=[0,-1,3,-10,5,9]
# res = sorted(list, reverse=False) sorted 是有返回值的
# print(res)

## 72、对list排序foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4],使用lambda函数从小到大排序
# foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]
# a = sorted(foo)
# print(a)

## 73.0  使用lambda函数对list排序foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]，输出结果为[0,2,4,8,8,9,-2,-4,-4,-5,-20]，正数从小到大，负数从大到小】（传两个条件，x<0和abs(x)）
# ls = [-5,8,0,4,9,-4,-20,-2,8,2,-4]
# ls1 = sorted(ls, key = lambda x: x <0)
# ls2 = sorted(ls,  key = lambda  x : (x<0,abs(x)))

# print(ls1)
# print(ls2)

## 74.0 列表嵌套字典的排序，分别根据年龄和姓名排序
# foo = [{"name":"zs","age":19},{"name":"ll","age":54},{"name":"wa","age":17},{"name":"df","age":23}]

# ls1 = sorted(foo, key = lambda x: x["name"])
# print(ls1)

# ls2 = sorted(foo, key= lambda x:x["age"],reverse=True)
# print(ls2)

## 75.0 列表嵌套元组，分别按字母和数字排序

## 76.0  列表嵌套排序 年龄数字相同  添加参数  Eg: foo =["as",12],["qw",12]  a =sorted(foo, key = lambda x : (x[1],x[0]))

## 77.0 根据键对字典排序  zip 函数

# dic = {"name":"zs","sex":"man", "city":"bj"}

# foo = zip(dic.keys(),dic.values()) ## 字典转换列表嵌套元组
# print(foo)
# foo = [i for i in foo]
# print(foo)
# b = sorted(foo,key=lambda  x: x[0]) ##字典嵌套元组排序
# new_dic = {i[0]:i[1] for i in b} ##字典推导式构造新字典
# print(new_dic)

## 78.0  根据键对字典排序  dic.items 和 zip(dic.keys(), dic.values()) 都是为了构造列表嵌套字典的结构 方便后面用sorted() 构造排序规则

# dic = {"name":"zs","sex":"man", "city":"bj"}
# foo = dic.items() ## 字典转换成
# b =sorted(dic.items(),key=lambda  x: x[0] )

## 79.0 列表推导式 字典推导式 生成器

# import random
# # ls = [i for i in range(10)]
# # ls1 = (i for i in range(10))
# ls2 = {k:random.randint(4,9) for k in ["a","b","c","d","e"]}
# # print(ls)
# # print(ls1)
# print(ls2)

## 80.0 根据字符串长度排序  lambda x : len(x)

## 81.0 举例说明SQL 注入和解决办法  当以字符串格式化书写方式的时候 乳沟用户输入的有 +SQL 语句 后面的SQL 语句会执行 比如例子中的SQLz注入会删除数据库的demo

# input_name = "zs"
# sql = 'selct * from demo where name = "%s"' % input_name
# print("正常查询", sql)

# input_name = "zs;drop database demo"
# sql = 'selct * from demo where name = "%s"' % input_name
# print("sql 注入会删除数据库demo", sql)
# 解决方式 通过传递参数的方式解决sql 注入
# params = [input_name]
# count = cls.execute('select * from goods where name = %s', params)

## 82.0 s="info:xiaoZhang 33 shandong",用正则切分字符串输出['info', 'xiaoZhang', '33', 'shandong']
# import re
# s="info:xiaoZhang 33 shandong"
# res = re.split(r":| ",s)
# print(res)

## 83.0 正则匹配以 163.com 结尾的邮箱
# import re
# email_list = ["1gdt@163.com","2@163.comhe","3.@qq.com"]
# for email in email_list:
#     ret = re.match("[\w]{4,20}@163\.com$",email)
#     if ret:
#         print("1",(email,ret.group()))
#     else:
#         print("2",email)

## 84.0递归求和 1+..+ 10
# def get_sum(num):
#     if num >=1:
#         res= num +get_sum(num-1)
#     else:
#         res =0

#     return res
# rs =get_sum(10)
# print(rs)

## 85.0 python 字典 和 Json 字符串相互转换方法
## json.dumps() 字典转换 Json 字符串  json.loads() json 转字典
# import json

# dic = {"name":"zs"}
# rs1 = json.dumps(dic)
# print(rs1, type(rs1))

# rs2 = json.loads(rs1)
# print(rs2,type(rs2))

## 86.0 myisam 和 InnoDB 的区别
## InnoDB 支持事务 MySAM 不支持 事务一种高级的处理方式 在一些列增删改查中之哟啊那个出错还可以回滚还原 Mylsam 是个查询以及插入为主的应用 InnoDB 适合频繁修改以及涉及安全性较高的应用 InnoDB 支持外键 MYLasm 不支持
## 对于自增长的字段 innoDB 中必须包含只有该字段的索引 但是在MYlSAM 表中可以和其他字段建立联合索引 清空整个表 InnnoDB 是一行一行的删除 效率低下  MyLSAM 会重新建表

## 87.0 统计字符串出现次数
 
# str1 = "1 2 3 4 5 3 4 3"
# rs = str1.count("3")
# print(rs)

## 88.0 字符串转换大小写 str.upper()  str.lower()

## 89.0 去除空格  
# str = "hello world ha ha"
# rs1 = str.replace(" ","")
# print(rs1)

# list = str.split(" ")
# re2 ="".join(list)
# print(re2)

## 90.0 正则匹配不是以4和7结尾的手机号 re.match(1\d{9}[0-3,5-6,8-9])

## 91.0 简述python 引用计数机制  python 垃圾回收主要以引用计数为主 标记清除和分代清除为辅的机制 当有1个变量保存了对象的引用时候 这个对象的引用计数就会增加1 当使用del 删除变量
## 指向的对象 如果该对象的引用计数不是1 比如是3 那么这个时候就会把该引用的计数减1 变成2 。。。

## 92.0 int("1.4") 报错 int(1.4) 输出1

## 93.0 PEP8 编码规范  顶级定义之间空两行 函数或者类  方法/类 与第一个方法之间 空一行 三引号进行注释Pycharm/eclopse 4 个空格 缩进

## 94.0 正则表达式匹配第一个url re.findall() / re.search()

## 95.0 正则匹配中文  re.compile(r'[\u4e00-\u9fa5]')

## 96.0 简述乐观锁和悲锁 拿数据认为别人会更改 /别人不会更改

## 97.0 r r+ rb rb+ 的区别和联系

## 98.0 Linux 命令重定向 > 和 >> Linux 允许命令将执行结果重定向到一个文件将本应显示在终端上的内容 输出/追加到指定文件中
## > 表示输出 会覆盖文件原有的内容 >> 表示追加 会将内容追加到已有文件的末尾

## 99.0 正则匹配<html></h1>www.itcast.cn</h1></html>  re.match(r"<(\w*)><\w*>.*?</\2></\1>)

## 100.0 python  传参数是值传递还是地址传递 python 中是地址(引用)传递 对于不可变类型 变量不能修改 运算不会影响变量自身 对于可变类型函数运算会更改传入的参数变量










