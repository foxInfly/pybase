"""
re是内置模块


"""
import re

# r"xx"  r表示是正则
# findall匹配所有符合规则的数据
s = "我的电话号码是18355135203,我小孩的电话是18834567890"
lst = re.findall(r"\d+", s)
it = re.finditer(r"\d+", s)
print(lst)
print(it)
for i in it:
    # print(i)
    print(i.group())
# 拿第一个
s2 = re.search(r"\d+", s)
print(s2.group())
# 从体开始匹配，以什么开头的意思
s3 = re.match(r"\d+", s)
print(s3)

# =================预加载========
obj = re.compile(r"\d+")
lst2 = obj.findall(s)
print(lst2)

# ================= 正则中的内容单独提取 ========

s3 = """
<div class='jay'><span id='1'>中国联通</span></div>
<div class='jj'><span id='23'>中国移动</span></div>
<div class='joly'><span id='3'>华为</span></div>
<div class='tom'><span id='10040'>比亚迪</span></div>
<div class='sy'><span id='10050'>晶合</span></div>
"""
# re.S:让.能匹配换行符；防止断掉
# obj2 = re.compile(r"<div class='.*?'><span id='\d+'>.*?</span></div>", re.S)
# (?P<wahaha>.*?)   .*?匹配到的内容会扔给wahaha;拿东西的时候用wahaha
obj2 = re.compile(r"<div class='.*?'><span id='\d+'>(?P<wahaha>.*?)</span></div>", re.S)
it3 = obj2.finditer(s3)
for i in it3:
    # print(i)
    # print(i.group())
    print(i.group("wahaha"))
