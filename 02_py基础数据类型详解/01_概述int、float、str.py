"""
int、float、bool
str
list
tuple
set
dict   java中的map
bytes
运算符
文件操作
"""
a = 10  # int
b = 10.5   # float
c = True   # bool   0是False  其他都是True  所以 while 1 也是死循环； 空str是False，非空都是True

# ==================== str ========================
"""
1. 字符串格式化
%s  字符串占位符，其实数据 bool也可以，万能占位
%d   数字占位符   e科学计数法
https://blog.csdn.net/LLC25802580/article/details/123095259
.1f  保留1位小数
2.1f  总长度2，小数点后1
-2.1f  左对齐  +右对齐  空格右对齐 0右对齐
-10s  表示10个左对齐的字符串占位符，不够后面用空格填充
"""
name = "lp"
age = 15
print("我叫%s,今年%d" % ("lp", 18))
print("我叫{},今年{}".format("lp", 18))
print(f"我叫{name},今年{age}")  # 3.5之后有的方法，推荐这个，好用

# 2.索引和切片
s = "hellO 我叫 lp，我住在合肥 "
print(s[2])  # 从0开始数
print(s[:])  # 从0到结尾
print(s[1:2])  # [1:2)
print(s[1:10:2])  # [1:10),间隔2
print(s[-1])  # 倒着数
print(s[1::2])  # 1开始，步长2个

# 3.字符串本身不是可变的数据，一般返回一个新的字符串
print(s.capitalize())  # 首字母大写()
print(s.lower())  # 全部小写   可用来忽略大小写操作
print(s.upper())  # 全部大写

# 4.切割和替换
print(s.strip())  # 取出两端空格   防止别人的名字误打空格，肉眼看不到
print(s.replace("lp", "mumu"))  # 把前面的替换成后面的
print(s.split("，"))  # 根据指定的字符，去切割，会把结果放到一个列表中；被切割的字符将不存在

# 查找和要替换
print(s.find("lp"))  # 返回查询的输入的位置，从0开始数;找不到返回-1
print(s.index("lp"))  # 返回查询的输入的位置，从0开始数；找不到报错
print("lp" in s)  # 在s中是否存在lp,  存在True   不存在False
print("lp" not in s)  # 在s中是否不存在lp,  不存在True   存在False
print(s.startswith("lp"))  # 是否以lp开头
print(s.endswith("lp"))  # 是否以lp结尾
print("23".isdigit())  # 是否是数字（0和正整数，Unicode数字，byte数字(单字节)，全角数字(双字节)，无error）digit
print("5".isdecimal())  # 是否是小数(检查是否仅有十进制的数字组成，Unicode数字，全角数字(双字节),byte error)decimal

print(len("lp"))  # len是个内置函数，返回字符串的长度
print("我叫".join("lp_123".split("_")))  # 把后面的列表用前面的字符串连接起来，相当于split的反操作

