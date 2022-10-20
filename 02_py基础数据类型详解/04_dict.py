"""
类似java的Map
key必须是可hash（不可变）的数据

"""
dic = {"name": "lp", "age": 18}
print(dic["name"])   # 查询,  不存在会报错。 确定key存在的时候，经常用这个，书写简单
print(dic.get("name"))   # 查询， 不存在，返回None（类型是NoneType），不会报错;判断有无的时候，经常用
dic["sex"] = "male"
dic[1] = "mumu"
dic["name"] = "qiong"  # key存在就是修改
dic.setdefault("name", "ll")  # 设置默认值（缺省值）；当没值的时候是这个，有值就用原有的
dic.pop("sex")   # 根据key删除
del dic["age"]   # 也是根据key删除，  不建议这种写法
print(dic)

# 循环嵌套
for key in dic:  # 默认是key
    print(key, dic[key])
print(dic.keys())
print(list(dic.values()))
print(list(dic.items()))
for key in dic.items():  # 默认是key
    print(key[0], key[1])
a, b = (1, 2)  # 元祖或者列表都可以这样操作，俗称解构（解包）
for a, b in dic.items():  # 默认是key
    print(a, b)

# 循环删除  循环的过程中不能删；临时列表做中介



