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
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time
# os是操作系统，sys代表python系统
# 拿到图片
web = Chrome()
# 如何让网站识别不了你是脚本程序跑起来的
# 1.chrom的版本号小于88
# window.navigator.webdriver=false  # 浏览器打开是false，驱动打开是true
# 程序启动浏览器的时候，向页面陷入JS代码，去掉window.navigator.webdriver
#  web = Chrome()
#
# web.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
#   "source": """
#    navigator.webdriver = undefined
#     Object.defineProperty(navigator, 'webdriver', {
#       get: () => undefined
#     })
#   """
# })
# web.get(xxxxxxx)

# 2.chrom的版本号大于等于88
option = Options()
# option.add_experimental_option('excludeSwitches', ['enable-automation'])
# option.add_argument('--disable-blink-features=AutomationControlled')
# web = Chrome(options=option)


# web = Chrome(chrome_options=opt)
# 2.用浏览器打开url;必须写全，包含https://
web.get("https://www.endata.com.cn/")
img = web.find_element(by=by.By.XPATH, value='xxxxxx').screenshot_as_png
# 访问超级鹰的接口进行解析

time.sleep(5)

# 拖拽
ActionChains(web).drag_and_drop(img, 300, 0).perform()


