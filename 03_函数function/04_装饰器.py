"""
装饰器：
    本质上是一个闭包
    作用：在不改变原有函数（代码）调用的条件下，给函数增加新的功能
    场景：用户登录、日志

"""


def guanjia(game):
    def inner():
        print("打开外挂")
        game()
        print("关闭外挂")

    return inner


@guanjia  # 相当于paly_wz = guanjia(paly_wz)
def paly_wz():
    print("鲁班哪里走")


@guanjia
def paly_lolo():
    print("德玛西亚！！！")


# paly_wz = guanjia(paly_wz)
paly_lolo = guanjia(paly_lolo)
paly_wz()
