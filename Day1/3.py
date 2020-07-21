## 16.0 <div class = "nam">中国 </div>, 用正则表达式匹配里面的内容（中国）， 其中class 的类名使不确定的
# import re
# ## . 代表可有可无， * 代表任意字符 满足类名可以变化
# str = '<div class = "nam">中国</div>'
# res = re.findall(r'<div class = ".*">(.*?)</div>', str)
# print(res)

## 17.0 python 中的 assert() 方法
# a =3
# assert(a>1)
# print("断言成功， 程序继续执行")

# assert(a >8)
# print("断言失败， 退出")

## 18.0 数据库常用数据   select distinct name from student

## 19.0 10 个常用的 Linux 命令  ls pwd cd touch rm mkdir tree cp mv cat more grep echo

## 20.0 python2 & python3 的区别
# 1.  Python3 使用print 必须要以小括号包裹打印内容 such as print（“hi”） python 即可以使用带小括号的方式， 也可以用一个空格分隔符进行打印 priint "hi"
# 2. python2 中 range(1,10) 返回列表, python 3 中返回迭代器， 节约内存
# 3. python2 使用ascill 编码， python3 使用utf-8 编码
# 4. Python 2 中Unicode 表示字符串序列,str 表示字节序列； python3 str 表示字符串序列， str 表示字节序列
# 5. Python2 中正常显示终未能需要引入codeing 声明， python3 不需要
# 6. python2 中raw_input() 函数, python3 中是 input() 函数

## 21.0 列出python 中可变数据类型和不可变数据类型
## 不可变数据类型： 数值型， 字符串型 string 和tuple() 不允许变量的值发生变化， 如果改变了变量的值， 相当于新建了一个对象， 而对于相同的值的对象，在内存中则只有有一个对象(一个地址) 可以用 id() 进行验证
# a =3
# b =3 
# print(id(a))
# print(id(b))
##可变数据类型 列表list 字典 dict 允许变量的值发生变化， 就是说如果对变量进行 appent, += 等操作, 只是改变了变量的值， 而不会新建一个对象，变量引用的对象的地址也不会变化, 不过对于相同的值的不同
## 对象，在内存中会存在不同的对象，即每个对象都有自己的地址， 相当于内存中对于相同值的对象保存了多份， 这里不存在引用计数， 使实实在在的对象

# a = [1,2]
# b = [1,2]
# print(id(a))
# print(id(b))

## 22.0 s ="ajldjlajfdljfddd"， 去重并且按照从小到大排序输出‘adfjl’ set 去重， 转换为 list, so让他 进行排序, reverse = False 是从小到大排序； list 四不可变烈性。 s.sort 没有返回值
# rs = list(set("ajldjlajfdljfddd"))
# rs.sort(reverse=False)
# rs = "".join(rs)
# print(rs)

## 23.0用lambda 函数实现两个数相乘
# sum = lambda  a, b: a *b
# print(sum(5,4))

## 24.0 字典根据建从小到大排序
# dic = {"name":"2", "name3":"4", "name1":"3"}

# rs = sorted(dic.items(), key=lambda  i: i[0], reverse=False)
# print(rs)
# print(dict(rs))

## 25.0 利用collection 库的 Count 方法统计字符串每个单词出现的次数 "kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"
# from collections import Counter
# a = "kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"
# res = Counter(a)
# print(res)
# print(type(res))

## 26.0 字符串 a  = "not 404 found 张三 99 深圳"， 用正则表达式过滤掉英文和数字， 输出张三 深圳
# import re
# a  = "not 404 found 1.1 张三 99 深圳"
# ls = a.split(" ")
# print(ls)

# res = re.findall('\d+\.?\d+|[a-zA-Z]+',a)
# for i in res:
#     if i in ls:
#         ls.remove(i)
# new_str = " ".join(ls)
# print(res)
# print(new_str)

## 27.0 filter 方法求出列表所有的奇数并且构造新列表 a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# fillter 函数用于过滤序列， 过滤掉不符合条件的元素, 返回由符合条件元素组成的新列表， 接受两个参数， 第一个为函数， 第二个为序列， 叙利厄的每个元素作为参宿传递给函数及逆行判断，返回False /True ， 最后将返回
# True 的元素放到新列表

# a =   [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# def fn(a):
#     return a %2 ==1
# print(list(filter(fn,a)))
# rs  = list(filter(lambda  x : x %2 ==1,a) )
# print(rs)

## 28.0 列表推导式求列表所有奇数并且构造新列表
# a =   [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# res = [x for x in a if x %2 ==1]
# print(res)

## 29.0 re.comple 的作用 是将正则表达式编译成一个对象， 加快速度， 并且重复使用

## 30.0 
print(type((1,)))
print(type((1)))
print(type(("1")))




