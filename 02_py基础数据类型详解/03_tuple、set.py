"""
tuple(元组) 不可变的列表
格式 (elm1,elm2,elm3...)
"""

t = ("lp", "mumu", "qiong")
# t[0] = "sen"  #会报错
# t1 = ("lp")  #因为()优先级高，这里会编译成字符串
t2 = ("lp",)  # 加个因为逗号，这里就是元祖了

t3 = ("lp", "mumu", ["aa", "b"])  # 第一层不可以动，但里面的列表是可以变的
t3[2][1] = "bb"


"""
set(集合) 无序、不可重复;只能放不可变的元素（可以hash，如字符串、数字、元祖、bool）
不可以嵌套
格式 {elm1,elm2,elm3...}
"""
s = {1, 3, "lp", "mumju", 4}
print(s)
# s = set()  # 空set
# s = tuple()  # 空tuple
# s = list()  # 空list
# s = str()  # 空str
s.add("qiong")
s.add("lp")
print(s)
s.pop()   # 默认弹出最后一个，由于无序，不可验证，很少用
s.remove(3)  # 指定删除  修改，就是先删除，再新增
print(s)

# ====== 交并差集 =======
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
print(s1 & s2)
print(s1.intersection(s2))
print(s1 | s2)
print(s1.union(s2))
print(s1 - s2)  # 左边有，右边没有
print(s2.difference(s1))  # 左边有，右边没有



