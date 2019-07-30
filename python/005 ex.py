import math

# for num in range(1,10000):
#     sum = 0
#     for factor in range(1, int(math.sqrt(num)+1)):
#         if num % factor == 0:
#             sum += factor
#             if factor >1 and num / factor != factor:
#                 sum += num / factor
#     if sum == num:
#         print(num)

for num in range(100, 1000):
    ge = num % 100
    shi = num // 10 % 10
    bai = num //100
    if num == ge ** 3 + shi ** 3 + bai ** 3:
        print(num)

first = 0
second = 1

for num in range(20):
    first, second = second, first + second
    print(first, end=' ')
