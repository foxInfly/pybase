"""
因为进程是资源级别，开进程会耗费太多的资源（内存），一般不建议多进程

"""
from multiprocessing import Process


def func():
    for i in range(1000):
        print(f"子进程{i}")


if __name__ == '__main__':
    # func()
    p = Process(target=func)  # 创建线程并给线程安排任务
    p2 = Process(target=func)  # 创建线程并给线程安排任务
    p3 = Process(target=func)  # 创建线程并给线程安排任务
    # t2 = MyThread()  # 创建线程并给线程安排任务
    p2.start()  # 多线程的状态为可以执行，具体什么时候执行，由CPU决定（分片）
    p3.start()
    for i in range(1000):
        print(f"main{i}")
