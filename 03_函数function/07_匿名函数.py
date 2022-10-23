"""
匿名函数：lambda表达式
语法规则：
    变量 = lambda 参数1,参数2...:返回值
简化代码
和内置函数一起用


"""


def func(a, b):
    return a + b


fn = lambda a, b: a + b
print(fn)
print(fn(2, 5))
