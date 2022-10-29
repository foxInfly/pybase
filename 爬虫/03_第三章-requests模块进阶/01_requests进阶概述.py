"""
header为http协议的请求头，一般存放一些和请求内容无关的数据，如安全信息等
通过requests发送的请求，可以把请求头信息放在headers中，也可以单独存放，最终由requests自动拼装成完整的http请求头

1.模拟浏览器登录->处理cookie
2.防盗链处理->抓取梨视频数据
3.代理->防止被封IP

综合训练：抓取网易云音乐评论信息
"""

"""
1.登录  获取cookie
2.带着cookie去请求

可以使用session进行球球  -> session可以认为是一连串的请求，在这个过程中的cookie不会丢失
"""
import requests

session = requests.session()
data = {
    "loginName": "19956500385",
    "password": "Lp123456"
}
#  1.登录
url = "https://passport.17k.com/ck/user/login"
resp = session.post(url, data=data)
# print(resp.text)
# print(resp.cookies)
headers = {
    "Cookie": "GUID=2730e5c3-1aac-4342-ab37-789c5f6b15c2; Hm_lvt_9793f42b498361373512340937deb2a0=1667011922; sajssdk_2015_cross_new_user=1; __bid_n=18421a74894fe6a0a54207; accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F13%252F93%252F96%252F99279693.jpg-88x88%253Fv%253D1667012143000%26id%3D99279693%26nickname%3D%25E4%25B9%25A6%25E5%258F%258BC2a3048cH%26e%3D1682564879%26s%3Dbd2bdc2fd5b00603; c_channel=0; c_csc=web; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2299279693%22%2C%22%24device_id%22%3A%2218421b5a314230-037c3384ef811-a7d193d-2073600-18421b5a315a2f%22%2C%22props%22%3A%7B%7D%2C%22first_id%22%3A%222730e5c3-1aac-4342-ab37-789c5f6b15c2%22%7D; Hm_lpvt_9793f42b498361373512340937deb2a0=1667014823"
}
# resp2 = session.get("https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919")
resp2 = requests.get("https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919", headers=headers)
print(resp2.json())

