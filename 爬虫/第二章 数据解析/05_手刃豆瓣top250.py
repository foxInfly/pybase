import requests
import re
import csv

url = "https://movie.douban.com/top250"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/93.0.4577.63 Safari/537.36 "
}
resp = requests.get(url, headers=headers)
page_content = resp.text
obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)'
                 r'</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp.*?<span '
                 r'class="rating_num" property="v:average">(?P<score>.*?)</span>.*?'
                 r'<span>(?P<people>.*?)人评价</span>', re.S)
it = obj.finditer(page_content)
no = 0
f = open("data.csv", mode="w")
# f = open("data.csv", mode="w", encoding="utf-8")
csvWriter = csv.writer(f)
for i in it:
    no += 1

    dic = i.groupdict()

    dic["year"] = dic["year"].strip()
    print(dic)
    csvWriter.writerow(dic.values())
    # print(no, i.group("name"), i.group("year").strip(), i.group("score"), i.group("people"))
f.close()
print("over")
