"""
一个类的组成部分：
    1.类属性  被该类的所有对象(类对象和实例对象)共享
    2.实例属性
    3.实例方法
    4.类方法    类能直接访问
    5.静态方法   类名直接访问,没有默认参数
对象的创建又叫类的实例化
语法：  实例名 = 类名()

在创建对象后，动态绑定属性和方法: 就是创建对象后再赋值,还可以添加（当没有这个属性或者方法的时候），这个比java灵活
"""


# 类外面的叫函数
def fu():
    print('function')


class Student:   # 在内存里会创建一个类对象，并开辟内存空间
    native_place = '合肥'  # 1.类属性

    def __init__(self, name, age):  # 2.name、age为实例属性

        self.name = name
        self.age = age

    # 3.实例方法
    def info(self):
        # print('my name is', self.name, ',age is', self.age, ", native_place is", self.native_place)
        print(f'my name is{self.name},age is{self.age}, native_place is{self.native_place}')

    # 4.类方法
    @classmethod
    def cm(cls):
        print('class method')

    # 5.静态方法
    @staticmethod
    def sm():
        print('static method')


# print(id(Student), hex(id(Student)).upper())  # 内存虚拟地址
# print(type(Student))  # 是什么类型
# print(Student)
# print("==============")
stu = Student("lp", "18")
# print(id(stu), hex(id(stu)).upper())
# print(type(stu))
# print(stu)
# print("==============")

stu.info()
print(Student.native_place)
print(stu.native_place)
Student.native_place = '北京'
print(Student.native_place)
print(stu.native_place)
stu.native_place = '上海'  # 这里涉及到作用域的问题，
print(Student.native_place)
print(stu.native_place)
# Student.cm()
# Student.sm()
# Student.info(stu)
fu()
stu.a = fu
stu.a()