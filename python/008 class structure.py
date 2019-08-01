class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('%s正在学习%s' % (self.name, course_name))

    def watch_movie(self):
        if self.age < 18:
            print('%s只能观看《熊出没》' % self.name)
        else:
            print('%s正在观看奥斯卡大电影' % self.name)

    def __str__(self):
        return '姓名：%s,年龄：%s' % (str(self.name), str(self.age))


stu1 = Student('骆昊', 38)
stu1.study('Python程序设计')
stu1.watch_movie()
stu2 = Student('王大锤', 15)
stu2.study('思想品德')
stu2.watch_movie()
print(stu2)
