import random

sumx = 0
for x in range(101):
    sumx += x

print(sumx)

"""
range(101)可以产生一个0到100的整数序列。
range(1, 100)可以产生一个1到99的整数序列。
range(1, 100, 2)可以产生一个1到99的奇数序列，其中的2是步长，即数值序列的增量。

"""
#
# answer = random.randint(1, 10)
# counter = 0
# while True:
#     counter += 1
#     number = int(input('请输入：'))
#     if number < answer:
#         print('大一点')
#     elif number > answer:
#         print('小一点')
#     else:
#         print('答对了！')
#         break
#
# print('你一共猜了%d次' % counter)

"""
上面的代码中使用了break关键字来提前终止循环，需要注意break只能终止它所在的那个循环，
这一点在使用嵌套的循环结构（下面会讲到）需要引起注意。
另一个关键字是continue，它可以用来放弃本次循环后续的代码直接让循环进入下一轮。

"""

from math import sqrt

num = int(input('请输入一个正整数：'))
end = int(sqrt(num))

is_prime = True

for x in range(2,end+1):
    if num %x == 0:
        is_prime = False
        break

if is_prime and num !=1:
    print('%d是素数' % num)
else:
    print('%d不是素数' % num)


x = int(input('请输入正整数1：'))
y = int(input('请输入正整数2：'))

if x > y:
    x, y = y, x
# 通过比较选取最小的数值x，最小公倍数 = 两数相乘/最小公约数
for factor in range(x, 0, -1):
    if x % factor ==0 and y % factor ==0:
        print('%d和%d的最大公约数是%d' % (x, y, factor))
        print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
        break



