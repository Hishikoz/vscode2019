def stringdata():
    str1 = 'hello world'
    print(len(str1))
    str2 = 'abc123456'
    print(str2[2:5])  #截取第三位到第五位
    print(str2[2:])
    print(str2[2::2])
    print(str2[::2])
    print(str2[::-1])   #字符串[开始索引：结束索引：步长]
    print(str2[-3:-1])  #截取倒数第三位与倒数第二位

"""
字符串   a    b     c     1    2    3    4   5   6
位数： 0    1    2     3     4    5
位数                                  -3  -2   -1

"""

def listdata1():
    list1 = [1, 3, 5, 7, 100]
    list1.insert(2, 400)
    list1.remove(3)
    del list1[0]
    print(list1)

def listdata2():
    fruits = ['grape', 'apple', 'strawberry', 'waxberry']
    fruits += ['pitaya', 'pear', 'mango']
    # 循环遍历列表元素
    for fruit in fruits:
        print(fruit.title(), end=' ')
    print()
    # 列表切片
    fruits2 = fruits[1:4]   #截取第二位到第四位
    print(fruits2)
    # fruit3 = fruits  # 没有复制列表只创建了新的引用
    # 可以通过完整切片操作来复制列表
    fruits3 = fruits[:]
    print(fruits3)
    fruits4 = fruits[-3:-1]
    print(fruits4)
    # 可以通过反向切片操作来获得倒转后的列表的拷贝
    fruits5 = fruits[::-1]
    print(fruits5)

def listdata3():
    f = [x + y for x in 'ABCDE' for y in '1234567']
    print(f)     # 用列表的生成表达式语法创建列表容器，元素已经准备就绪所以需要耗费较多的内存空间
    g = (x for x in range(1,100))
    print(g)    #通过生成器可以获取到数据但它不占用额外的空间存储数据

"""
yield生成器介绍：https://blog.csdn.net/mieleizhi0522/article/details/82142856
"""
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a

def listdata4():
    for val in fib(20):
        print(val)

#listdata4()