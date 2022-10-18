money = input("请输入您的余额：")
money = int(money)
if money > 30:
    print("钱够用")
elif money > 50:
    print("钱很够用")
else:
    print("钱不够用")

print("over。。")

# ====================================
# for 主要面对可迭代的东西
s = "我叫lp"
for c in s:
    print("for循环：", c)
#
for i in range(10):  # 0~9
    print("for range1: ", i)

#
for i in range(3, 10):  # 3~9
    print("for range2: ", i)

# 带步长
for i in range(3, 10, 2):  # 3~9,每次间隔2个，就是3,5,7,9
    print("for range2: ", i)
# ===================
i = 1
while i < 10:
    print("喷死你 ", i)
    i = i+1

# break：退出当前循环
# continue：进入循环的下一环
# pass   主要用于保证完整性，类似于Java的TODO  但是不一样，就是当前有这段代码，但是会跳过，继续下面的代码，但不会跳出if判断

