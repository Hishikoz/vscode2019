import re

def test():
    username = input('请输入用户名：')
    qq = input('请输入QQ号：')

    m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$', username)
    if not m1:
        print('请输入有效的用户名。')

    m2 = re.match(r'^[1-9]\d{4,11}$', qq)
    if not m2:
        print('请输入有效的QQ号.')
    if m1 and m2:
        print('你输入的信息是有效的!')

"""
^匹配字符串开始，$匹配结尾
https://deerchao.net/tutorials/regex/regex.htm
https://github.com/jackfrued/Python-100-Days/blob/master/Day01-15/12.%E5%AD%97%E7%AC%A6%E4%B8%B2%E5%92%8C%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F.md
"""

def main():
    test()

if __name__ == '__main__':
    main()

