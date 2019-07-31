def stringdata():
    str1 = 'hello world'
    print(len(str1))
    print(str1.find('or'))
    print(str1[7:])
    str2 = 'abc123456'
    print(str2[2:5])  #截取第三位到第五位
    print(str2[2:])
    print(str2[2::2])
    print(str2[::2])
    print(str2[::-1])   #字符串[开始索引：结束索引：步长]
    print(str2[-3:-1])  #截取倒数第三位与倒数第二位

#stringdata()
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

def listdata5():
    days = [[1,2],[3,4]][False]
    print(days[0])

listdata5()

"""
Python 的元组与列表类似，不同之处在于元组的元素不能修改，
顾名思义，我们把多个元素组合到一起就形成了一个元组，
所以它和列表一样可以保存多条数据。下面的代码演示了如何定义和使用元组。
元组中的元素是无法修改的，事实上我们在项目中尤其是多线程环境（后面会讲到）中可能更喜欢使用的是那些不变对象
（一方面因为对象状态不能修改，所以可以避免由此引起的不必要的程序错误，简单的说就是一个不变的对象要比可变的对象更加容易维护；
另一方面因为没有任何一个线程能够修改不变对象的内部状态，一个不变对象自动就是线程安全的，这样就可以省掉处理同步化的开销。
一个不变对象可以方便的被共享访问）。所以结论就是：如果不需要对元素进行添加、删除、修改的时候，可以考虑使用元组，
当然如果一个方法要返回多个值，使用元组也是不错的选择。元组在创建时间和占用的空间上面都优于列表。
我们可以使用sys模块的getsizeof函数来检查存储同样的元素的元组和列表各自占用了多少内存空间，
这个很容易做到。我们也可以在ipython中使用魔法指令%timeit来分析创建同样内容的元组和列表所花费的时间，
"""
def tupledata1():
    t = ('骆昊', 38, True, '四川成都')
    # t[0] = '王大锤'
    # print(t)
    # 将元组转换成列表
    person = list(t)
    print(person)
    # 列表是可以修改它的元素的
    person[0] = '李小龙'
    person[1] = 25
    print(person)

#tupledata1()

def setdata1():
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}

    print(set1 & set2)
    print(set1 | set2)
    print(set1 - set2)
    print(set1 ^ set2)

#setdata1()

def dictdata1():
    scores = {'骆昊': 95, '白元芳': 78, '狄仁杰': 82}
    print(scores)

#dictdata1()

def test1():
    persons = [True] * 30
    counter, index, number = 0, 0, 0
    while counter < 15:
        if persons[index]:
            number += 1
            if number == 9:
                persons[index] = False
                print(index)
                counter += 1
                number = 0
        index += 1
        index %= 30
    for person in persons:
        print('基' if person else '非', end='')

test1()