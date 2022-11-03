"""
将数据（属性）和行为（方法）封装到类对象中，提高程序的安全性

"""
class Student:   # 在内存里会创建一个类对象，并开辟内存空间
    native_place = '合肥'  # 1.类属性

    def __init__(self, name, age):  # 2.name、age为实例属性

        self.name = name
        self.__age = age   # 两个下划线，外部就访问不到了


stu = Student('lp', 16)
print(dir(stu))
print(stu._Student__age)  # 还是能访问到的，就得靠程序员的自觉性了

print(stu.__str__())