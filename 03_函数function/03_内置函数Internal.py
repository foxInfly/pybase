"""
内置函数：python提供好的，可以直接拿来用的

https://www.processon.com/mindmap/63528e591efad44c791e058f

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
print(id("中"))

