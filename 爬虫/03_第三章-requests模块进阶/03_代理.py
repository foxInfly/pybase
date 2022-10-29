"""
原理：通过第三方的机器去发送请求
    代理网站：站大爷
        https://www.zdaye.com/
"""

import requests


# ip port
proxies = {
    # "http": "218.60.8.83:3129",
    # "https": "218.60.8.83:3129",
    "https": "https://218.60.8.83:3129"  # 有的版本需要加上https:

}


# resp = requests.get("https://www.baidu.com")
resp = requests.get("https://www.baidu.com", proxies = proxies)  # 加代理：原理就是先发给代理，代理再转发
print(resp.text)
