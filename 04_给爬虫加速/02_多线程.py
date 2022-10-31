"""
线程：执行单位，一个进程下面至少一个线程，
进程：是资源，存放一个程序的资源（内存），如一个QQ就是一个进程

"""
from threading import Thread  # 线程类


def func(name):
    for j in range(50):
        print(f"{name}-{j}")


# 这里线程的第二种写法，继承Thread
class MyThread(Thread):
    # def __init__(self, name):
    #     # self.name = name
    #     super.__init__(self,name=name)
    def run(self):
        for k in range(20):
            print(f"{self.name}子线程{k}")


# 启动一个程序，默认会生成一个主线程
if __name__ == '__main__':
    # func()
    t = Thread(target=func, args=("lp",))  # 创建线程并给线程安排任务,传参必须是元组
    t2 = MyThread()  # 创建线程并给线程安排任务
    t.start()  # 多线程的状态为可以执行，具体什么时候执行，由CPU决定（分片）
    t2.start()
    for i in range(20):
        print(f"main{i}")
