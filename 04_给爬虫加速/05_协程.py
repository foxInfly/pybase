"""

一般情况下，当程序处于IO操作时，线程都处于阻塞状态
协程：当程序遇见了IO操作时，可以选择性额切换到其他任务上
"""
import time
import asyncio


# async  异步协程
async def fn():
    print("111")
    await asyncio.sleep(2)  # 当前线程处于阻塞状态，CPU是不会为我工作的
    print("111")
async def fn2():
    print("22")
    # time.sleep(3)  # 当程序出现了同步操作的时候，异步就中断了
    await asyncio.sleep(3)  #await是挂起来，这样可以切换别的任务了
    print("22")
async def fn3():
    print("33")
    await asyncio.sleep(4)  # await 一般放在协程对象前
    print("33")


if __name__ == '__main__':
    f = fn()
    f2 = fn2()
    f3 = fn3()
    print(f)
    tasks = {
        f, f2, f3
    }
    # asyncio.run(f)  # 执行协程，需要asyncio模块的支持
    # 一次启动多个任务（协程）
    t1 =time.time()
    asyncio.run(asyncio.wait(tasks))
    print(time.time()-t1)