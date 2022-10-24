
# 代开网址
from urllib.request import urlopen

url = "http://www.baidu.com"
resp = urlopen(url)  # <http.client.HTTPResponse object at 0x0000019D81137BE0>

# resp.read()  # 这里读取出来的是二进制

# print(resp.read().decode("utf-8"))
with open("mybaidu.html", mode="w") as f:
    f.write(resp.read().decode("utf-8"))

print("over!")
