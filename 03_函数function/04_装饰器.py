"""
装饰器：
    本质上是一个闭包
    作用：在不改变原有函数（代码）调用的条件下，给函数增加新的功能
    场景：用户登录、日志

"""


# def guanjia(game):
#     # def inner(username, password):
#     def inner(*args, **kwargs):  # args是元组，kwargs是dict
#         print("打开外挂")
#         # game(username, password)
#         game(*args, **kwargs)  # 打散再返回回去
#         print("关闭外挂")
#
#     return inner
#
#
# @guanjia  # 相当于paly_wz = guanjia(paly_wz)
# def paly_wz(username, password):
#     print("鲁班哪里走", username, password)
#
#
# @guanjia
# def paly_lolo(username, password, hero):
#     print("德玛西亚！！！", username, password, hero)


# paly_wz = guanjia(paly_wz)
# paly_lolo = guanjia(paly_lolo)
# paly_wz("lp", "123")
# paly_lolo("lp", "123", "盖伦")

# ==============返回值============

def guanjia(game):
    # def inner(username, password):
    def inner(*args, **kwargs):  # args是元组，kwargs是dict
        print("打开外挂")
        # game(username, password)
        ret = game(*args, **kwargs)  # 打散再返回回去
        print("关闭外挂")
        return ret

    return inner


@guanjia  # 相当于paly_wz = guanjia(paly_wz)
def paly_wz(username, password):
    print("鲁班哪里走", username, password)
    return "100元"


@guanjia
def paly_lolo(username, password, hero):
    print("德玛西亚！！！", username, password, hero)
    return "99元"


# paly_wz = guanjia(paly_wz)
# paly_lolo = guanjia(paly_lolo)
print(paly_wz("lp", "123"))
print(paly_lolo("lp", "123", "盖伦"))

login_flag = False


def login_verify(fn):
    def inner(*args, **kwargs):
        global login_flag
        if not login_flag:
            print("还未完成登录操作")
            # 登录验证
            while 1:
                username = input(">>>")
                password = input(">>>")
                if username == "lp" and password == "123":
                    print("登陆成功")
                    login_flag = True
                    break
                else:
                    print("登陆失败,请重新登录！")
        ret = fn(*args, **kwargs)
        return ret

    return inner


@login_verify
def add():
    print("添加员工信息")


@login_verify
def delete():
    print("删除员工信息")


@login_verify
def update():
    print("更新员工信息")


def search():
    print("添加查询员工信息")


add()
delete()
update()
