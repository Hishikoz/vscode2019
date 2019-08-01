from abc import ABCMeta, abstractmethod

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)

    def watch_av(self):
        if self._age >= 18:
            print('%s正在观看爱情动作片.' % self._name)
        else:
            print('%s只能观看《熊出没》.' % self._name)

"""
我们之前的建议是将属性命名以单下划线开头，通过这种方式来暗示属性是受保护的，
不建议外界直接访问，那么如果想访问属性可以通过属性的getter（访问器）和setter（修改器）方法
进行对应的操作。如果要做到这点，就可以考虑使用@property包装器来包装getter和setter方法，
使得对属性的访问既安全又方便。
"""

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def study(self, course):
        print('%s的%s正在学习%s' % (self._grade, self._name, course))

class Pet(object, metaclass=ABCMeta):
    """宠物"""

    def __init__(self, nickname):
        self._nickname = nickname

    @abstractmethod
    def make_voice(self):
        """发出声音"""
        pass


class Dog(Pet):
    """狗"""

    def make_voice(self):
        print('%s: 汪汪汪...' % self._nickname)


class Cat(Pet):
    """猫"""

    def make_voice(self):
        print('%s: 喵...喵...' % self._nickname)


def main():
    person = Person('王大锤', 12)
    person.play()
    person.age = 22
    person.sex = '男'
    print(person.sex)
    person.play()

    stu = Student('王小锤', 15, '初三')
    stu.study('数学')
    stu.watch_av()

    pets = [Dog('旺财'), Cat('凯蒂'), Dog('大黄')]
    for pet in pets:
        pet.make_voice()

"""
通过abc模块的ABCMeta元类和abstractmethod包装器来达到抽象类的效果，
如果一个类中存在抽象方法那么这个类就不能够实例化（创建对象）。
上面的代码中，Dog和Cat两个子类分别对Pet类中的make_voice抽象方法进行了重写
并给出了不同的实现版本，当我们在main函数中调用该方法时，这个方法就表现出了多态行为
（同样的方法做了不同的事情）。
"""


if __name__ == '__main__':
    main()
