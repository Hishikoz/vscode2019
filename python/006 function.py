# 在参数名前面的*表示args是一个可变参数
# 即在调用add函数时可以传入0个或多个参数
def add(*args):
    total = 0
    for val in args:
        total += val
    return total

print(add())
print(add(1,2,3))

def is_palindrome(num):
    temp = num
    total = 0
    while temp > 0:
        total = total *10 + temp % 10
        temp //=10
    return  total == num

if __name__ == '__main__':
    num = int(input('请输入正整数：'))
    if is_palindrome(num):
        print('%d是回文数' % num)

"""
如果我们导入的模块除了定义函数之外还中有可以执行代码，
那么Python解释器在导入这个模块时就会执行这些代码，
事实上我们可能并不希望如此，因此如果我们在模块中编写了执行代码，
最好是将这些执行代码放入如下所示的条件中，这样的话除非直接运行该模块，
if条件下的这些代码是不会执行的，因为只有直接执行的模块的名字才是“__main__”。
"""