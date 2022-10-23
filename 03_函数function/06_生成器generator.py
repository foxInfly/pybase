"""
推导式：简化代码
    1.列表推导式
        [数据 for循环 if判断]
    2.字典推导式
        {k:v for循环 if判断}
    3.集合推导式
        {数据 for循环 if判断}

    (数据 for循环 if判断) -> 不是元组推导式（根本没有元组推导式），是生成器表达式

生成器的本质就是迭代器,像迭代器一样使用他们
创建生成器的两种方案：
    1.生成器函数
        有个关键字yield,可以认为代替了return的
    2.生成器表达式
yield(生成):出现该关键字，就是一个生成器函数

作用：
    1.数据量大的时候，一次处理不完，就可以用生成器，分段执行

"""

# lst0 = []
# for i in range(100):
#     lst0.append(i)
# lst0 = [i for i in range(10)]
# lst0 = [i for i in range(1, 10, 2)]
lst0 = [i for i in range(10) if i % 2 == 1]
print(lst0)
lst1 = [f"衣服{i}" for i in range(50)]
dic0 = {i : lst1[i] for i in range(len(lst1))}
print(dic0)


def func():
    print("123")
    # return 999
    yield 999  # 只有执行next的时候，才会执行；1.可以返回数据；2.可以分段执行函数
    print("456")
    yield 666


ret = func()
print(ret)
print(ret.__next__())
print(ret.__next__())


def order():
    lst = []
    for i in range(10000):
        lst.append(f"衣服{i}")
        if len(lst) == 50:
            yield lst
            lst = []
# gen = (f"衣服{i}" for i in range(10000) if len(lst) == 50)


gen = order()
print(gen)
print(gen.__next__())
print(gen.__next__())
# i**2代表i的2次方
gen2 = (i**2 for i in range(10))
print(gen2)
print(gen2.__next__())
print(gen2.__next__())
print(gen2.__next__())
print(gen2.__next__())
print(list(gen2))   # list==>for ==> iterator

