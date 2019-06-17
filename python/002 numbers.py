"""
Use variables to save data and calculate results
"""

import math

# a = 321
# b = 123

# print(a + b)
# print(a // b)
# print(a % b)

# c = int(input('c = '))
# d = int(input('d = '))
# print('%d + %d = %d' % (c, d, c+d))

# flag1 = 3 > 2
# flag2 = 2 < 1
# flag3 = flag1 and flag2
# flag4 = flag1 or flag2
# flag5 = not flag1
# print("flag1 = ", flag1)
# print("flag2 = ", flag2)
# print("flag3 = ", flag3)
# print("flag4 = ", flag4)
# print("flag5 = ", flag5)
# print(flag1 is True)
# print(flag2 is not True)

# f = float(input('请输入华氏温度 = '))
# c = (f-32)/1.84
# print('摄氏温度 = %.1f' % c)

# radius = float(input('请输入圆的半径：'))
# area = math.pi * (radius ** 2)
# print('圆的周长是： %.2f' % area)

year = int(input('请输入年份：'))
is_leap = (year % 4 ==0 and year %100 !=0 or year % 400 ==0)
print(is_leap)