"""
1.2022必看热片
2.https://www.dytt89.com/

"""
import requests
import re

domain = "https://www.dytt89.com/"
# verify=False 不错校验（去掉安全任验证）
resp = requests.get(domain, verify=False)
resp.encoding = "gb2312"  # 指定编码
page_content = resp.text
obj = re.compile(r'2022必看热片.*?<ul>(?P<url>.*?)</ul>', re.S)
obj2 = re.compile(r"<li><a href='(?P<href>.*?)' title=", re.S)

it = obj.finditer(page_content)
child_herf_list = []
for i in it:
    url = i.group("url")
    # print(url)
    herf = obj2.finditer(url)
    for h in herf:
        child_herf = domain + h.group("href").strip("/")
        child_herf_list.append(child_herf)
        # print(child_herf)

obj3 = re.compile(r"<li><a href='(?P<href>.*?)' title=", re.S)
for herf in child_herf_list:
    child_resp = requests.get(domain, verify=False)
    child_resp.encoding = "gb2312"  # 指定编码
    print(herf)
    page_content = child_resp.text

    print(page_content)  # 有弹框，55555
    break

