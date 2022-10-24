"""
内置函数：python提供好的，可以直接拿来用的

https://www.processon.com/mindmap/63528e591efad44c791e058f


zip:合并可以迭代的内容

"""
print(bin(22))
print(oct(22))
print(hex(22))
print(abs(-22))
print(pow(10, 2))
print(ord("中"))
print(chr(20013))
# 路径中有中文，会报错
# for i in range(65536):
#     print(chr(i)+" ", end="")
print(hash("中"))
print(id("中"))  # 拿内存地址

# ================ zip ================
lst1 = ["赵本山", "苏有朋"]
lst2 = [40, 42]
lst3 = ["卖拐", "情深深雨蒙蒙"]
result = zip(lst1, lst2, lst3)
print(result)
# print(dir(result))
print(list(result))

# a = 188
# print(locals())  # 此时写在全局范围内，看到的就是全局作用域


# 平常用的不多
def func():
    a = 100
    print(locals())  # 此时写在局部范围内，看到的就是当前局部作用域
    print(globals())  # 全局内容


func()




