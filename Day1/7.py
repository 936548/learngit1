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
foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]
a = sorted(foo)
print(a)
