"""
线程：执行单位，一个进程下面至少一个线程，
进程：是资源，存放一个程序的资源（内存），如一个QQ就是一个进程

"""
from threading import Thread  # 线程类


def func():
    for i in range(10):
        print("func", i)


# 启动一个程序，默认会生成一个主线程
if __name__ == '__main__':
    # func()
    t = Thread(target=func)  # 创建线程并给线程安排任务
    t.start()  # 多线程的状态为可以执行，具体什么时候执行，由CPU决定（分片）
    for i in range(10):
        print("main", i)


# 这里线程的第二种写法，继承Thread
class MyThread(Thread):
    def run(self):
        pass
