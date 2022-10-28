"""
<h1 align="center"> i love you </h1>
h1:  标签
align:  属性
center: 属性值

bs4属于第三方安装包
  pip install bs4
  pip install bs4 -i https://pypi.tuna.tsinghua.edu.cn/simple
    beautifulsoup4-4.11.1-py3-none-any.whl
"""
import requests
from bs4 import BeautifulSoup


url = "https://movie.douban.com/top250"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/93.0.4577.63 Safari/537.36 "
}
# resp = requests.get(url, headers=headers)
# print(resp.text)
# page = BeautifulSoup(resp.text, "html.parser")
# find(标签，属性=值)
# findall(标签，属性=值)
# src = page.findAll("span", class_="title")  # class是python的关键字;可以加一个_下划线区别
# print(src)

url2 = "https://www.umei.cc/bizhitupian/weimeibizhi/"
resp = requests.get(url2, headers=headers)
resp.encoding = "utf-8"
# print(resp.text)
page = BeautifulSoup(resp.text, "html.parser")
list1 = page.find("div", id="infinite_scroll").findAll("a", class_="img_album_btn")
# list1 = page.findll("div", class_="item masonry_brick")
# print(list1)
for i in list1:
    herf = i.get("href")
    print(herf)





