"""
list 有序、可重复的集合，英文逗号隔开
格式[elm1,elm2,elm3...]
"""

lst = ["lp", "mumu", "qiong", "lin", "sen"]
print(lst[0])
print(lst[0:])
print(lst[0:1])
print(lst[0:len(lst):2])
print(lst[:2])  # [0,2)
print(lst[::2])  # 步长2
print(lst[1::2])  # 1开始  步长2
print("lp" in lst)  # 判断，还可以for循环

# ============== 增删改查 ===============
lst.append("zhudy")   # 在后面追加
lst.insert(1, "pp")   # 1的后面插入
lst.extend(["aa", "bb", "aa"])   # 在列表的最后面追加新的列表
print(lst)
print(lst.pop(1))  # 弹出第几个元素，从0开始数
lst.remove("aa")  # 移走匹配到的第一个value， 返回None，找不到也不会报错
lst[5] = "sensen"  # 修改
print(lst)

# 排序
lst.sort()  # 默认升序
print(lst)
lst.sort(reverse=True)  # 降序
print(lst)

# 可以嵌套
lst.append(["zhudy", "dd"])   # 在后面追加
print(lst)
print(lst[8][1])

# 循环删除，因为是连续的，其实类似java的数组，删除一个，后面的会移到前面（下标就变了）
# 方式一   准备一个临时列表（作为循环条件），再去真正列表去删除
# 方式二   自己研究





