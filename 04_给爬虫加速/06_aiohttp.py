"""
requests.get()是同步操作
异步aiohttp
pip install aiohttp -i https://pypi.tuna.tsinghua.edu.cn/simple
    aiohttp-3.8.3-cp38-cp38-win_amd64.whl (324 kB)
    multidict-6.0.2-cp38-cp38-win_amd64.whl (28 kB)
    aiosignal-1.2.0-py3-none-any.whl (8.2 kB)
    yarl-1.8.1-cp38-cp38-win_amd64.whl (56 kB)
    async_timeout-4.0.2-py3-none-any.whl (5.8 kB)
    frozenlist-1.3.1-cp38-cp38-win_amd64.whl (34 kB)
    attrs-22.1.0-py2.py3-none-any.whl (58 kB)

"""
import asyncio
import aiohttp


urls = []


async def aiodownload(url):
    # aiohttp.ClientSession  # requests
    name = url.rsplit("/", 1)[1]  #从右边切1次，去取第二个
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            with open(name , mode="wb") as f:
                f.write(await resp.content.read())


async def main():
    tasks = []
    for url in urls:
        tasks.append(aiodownload(url))
    await asyncio.wait(tasks)

if __name__ == '__main__':
    asyncio.run(main())
