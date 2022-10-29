"""
1.服务器做了防盗链处理；加工
    1.拿到contId
    2.拿到VidoStatus返回的json  -> srcURL
    3.根据第一步修改srcURL
    4.下载视频
"""
import requests

url = "https://www.pearvideo.com/video_1693651"
contId = url.split("_")[1]
print(contId)
videoStatus = "https://www.pearvideo.com/videoStatus.jsp?contId=1693651&mrd=0.3794015352299973"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/93.0.4577.63 Safari/537.36 ",
    # "contId": contId,
    "Referer": url  # 这里就是防盗链:溯源，当前本次请求的上一级（谁发起的请求）
}
resp = requests.get(videoStatus, headers=headers)
# print(resp.headers)
dic = resp.json()
print(dic)
srcURL = dic["videoInfo"]["videos"]["srcUrl"]
systemTime = dic["systemTime"]
print(systemTime)
srcURL = srcURL.replace(systemTime, f"cont-{contId}")
print(srcURL)
# 下载视频
with open("a.mp4", mode="wb") as f:
    f.write(requests.get(srcURL).content)


