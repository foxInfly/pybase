"""
模块：Modules
    就是一个.py的文件；可以包含n多个类，函数，语句a=10
导入模块
    import 模块名  [as 别名]
    from 模块名称 import 函数/变量/类


以主程序的形式运行：
    在每个模块的定义中，都包含一个记录模块名称的变量，__name__；程序可以检查变量
    以确定它在哪个模块中执行。如果一个模块不是被导入到其他程序中时，__name__="__main__"

包：
    一个分层次的目录结构，它将一组功能相近的模块放在一起
    作用：艾玛规范、避免模块名称冲突
包与目录的区别：
    包含__init__.py文件的目录称为包
    目录里通常不含__init__.py文件

内置模块：
    sys     与python解释器及其环境操作相关的标准库
        sys.getsizeof()
    time    与实践相关的库
        time.time()
        time.sleep()
    os      访问操作系统相关的库

    calendar    日期相关
    urllib      读取网路数据
        urllib.request.urlopen
    json    json相关
    re          正则
    math    标准算数运算
    decimal 精确控制运算精度、有效位数、四舍五入的十进制运算
    logging     日志

pip install schedule -i https://pypi.tuna.tsinghua.edu.cn/simple
    schedule-1.1.0-py2.py3-none-any.whl (10 kB)

"""
import schedule
import time


def job():
    print(time.time())


schedule.every(3).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)

# if __name__ == '__main__':
#     pass
