"""
1.图像识别,难度高
2.选择互联网上成熟的验证码破解工具，如超级鹰
    注册，免费试用，软件ID（远程连接用）
    开发文档
    下载demo
    copy  (默认python2的代码，自己修改下)

"""
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import by
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time

# 拿到图片
web = Chrome()
# web = Chrome(chrome_options=opt)
# 2.用浏览器打开url;必须写全，包含https://
web.get("https://www.endata.com.cn/")
img = web.find_element(by=by.By.XPATH, value='xxxxxx').screenshot_as_png
# 访问超级鹰的接口进行解析





