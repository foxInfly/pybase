"""
不是python自带的模块,进入terminal
安装：pip install requests   （在线安装）对url的封装
比较慢的话，可以使用国内镜像，如清华源\阿里源（百度搜索后，操作）
    requests-2.28.1-py3-none-any.whl (62 kB)
    charset_normalizer-2.1.1-py3-none-any.whl
    certifi-2022.9.24-py3-none-any.whl (161 kB)
    idna-3.4-py3-none-any.whl (61 kB)
    urllib3-1.26.12-py2.py3-none-any.whl (140 kB)
    urllib3-1.26.12-py2.py3-none-any.whl (140 kB)
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple    requests

"""
import requests

'''
query = "周杰伦"
url = f"https://www.sogou.com/web?query={query}"

# 处理一个小小的反爬
dic = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/93.0.4577.63 Safari/537.36 "
}
resp = requests.get(url, headers=dic)

print(resp)
print(resp.text)  # 页面源代码
'''

"""
kw = "dog"
dic = {
    "kw": kw
}
url1 = "https://fanyi.baidu.com/sug"
resp = requests.post(url1, data=dic)
print(resp)
# print(resp.text)  # 页面源代码
print(resp.json())  # 将服务器返回的内容直接处理成json
"""

url2 = "https://movie.douban.com/j/chart/top_list"
param = {
    "type": "24",
    "interval_id": "100:90",
    "action": "",
    "start": "0",
    "limit": "20"
}
# 使用了反爬
dic = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/93.0.4577.63 Safari/537.36 "
}

resp = requests.get(url2, headers=dic, params=param)
print(resp)
print(resp.request.headers)
print(resp.request.url)

print(resp.json())

resp.close()   # 不关的，话，会和服务器有一个连接，连接的数量是有限的，容易把服务器搞崩；1.keepAlive=False;2.直接close（）

