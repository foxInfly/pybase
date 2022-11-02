"""
程序连到浏览器，浏览器解析后，我们再爬
selenium：原本被设计成做自动化测试用的
    可以打开浏览器，像人一样去操作浏览器，程序员可以从selenium中直接提取网页上的各种信息
环境搭建：
    1.pip install selenium -i https://pypi.tuna.tsinghua.edu.cn/simple
        selenium-4.5.0-py3-none-any.whl (995 kB)
        trio-0.22.0-py3-none-any.whl(384 kB)
        trio_websocket-0.9.2-py3-none-any.whl (16 kB)
        sniffio-1.3.0-py3-none-any.whl (10 kB)
        sortedcontainers-2.4.0-py2.py3-none-any.whl (29 kB)
        outcome-1.2.0-py2.py3-none-any.whl (9.7 kB)
        exceptiongroup-1.0.0-py3-none-any.whl (12 kB)
        async_generator-1.10-py3-none-any.whl (18 kB)
        wsproto-1.2.0-py3-none-any.whl (24 kB)
        PySocks-1.7.1-py3-none-any.whl (16 kB)
        h11-0.14.0-py3-none-any.whl (58 kB)
    2.下载浏览器驱动
        https://registry.npmmirror.com/binary.html?path=chromedriver/
        找和自己浏览器版本一样的下载，如我的：版本 93.0.4577.63（正式版本） （64 位
        https://registry.npmmirror.com/binary.html?path=chromedriver/93.0.4577.63/
        根据自己的系统选择性下载
            把解压缩后的浏览器驱动，chromedriver放在python解释器所在的文件夹(pychar跑一下，会显示出路径来)

"""

# 让selenium启动一个浏览器
from selenium.webdriver import Chrome
from selenium.webdriver.common import by
from selenium.webdriver.common.keys import Keys
import time

# 1.创建浏览器对象
web = Chrome()
# 2.用浏览器打开url;必须写全，包含https://
web.get("https://www.lagou.com/")
# ele = web.find_element(by=by.By.XPATH, value='//*[@id="changeCityBox"]/p[2]/a')  # 全国
ele = web.find_element(by=by.By.XPATH, value='//*[@id="changeCityBox"]/ul/li[1]/a')  # 北京
ele.click()  # 点击事件
time.sleep(1)  # 让浏览器缓一缓，程序比较快，那边还没加载出来，可能会报错（如ajax的）
# 找到输入框，输入python ==> 输入回车或者年级搜索
# 找到搜索框，输入python并单击回车
web.find_element(by=by.By.XPATH, value='//*[@id="search_input"]').send_keys("python", Keys.ENTER)
time.sleep(1)
# 查找存放数据的位置，进行数据提取
# li_list = web.find_element(by=by.By.XPATH, value='//*[@id="jobList"]/div[1]/ul/li[1]')
# li_list = web.find_element(by=by.By.XPATH, value='//*[@id="jobList"]/div[1]/div[1]')
li_list = web.find_elements(by=by.By.XPATH, value='//*[@id="jobList"]/div[1]/div')
print(web.title)

for i in li_list:
    work = i.find_element(by=by.By.TAG_NAME, value='a').text  # 找a标签的文本
    # work = i.find_element(by=by.By.XPATH, value='./div/div/div[1]/a').text  # 找a标签的文本
    # salry = i.find_element(by=by.By.XPATH, value='./div/div/div[2]/span').text  # 找salry
    # print(f"woke:{work},\tsalry:{salry}")
    print(f"woke:{work},\tsalry:")
# 在selenium的眼中，新窗口是默认不切换过来的，需要窗口切换
web.switch_to.window(web.window_handles[-1])  # -1j就是最后一个窗口


web.close()  # 关闭子窗口
web.switch_to.window(web.window_handles[0])  # 切换到第一个窗口

# 如果网页遇到了iframe该如何处理；先拿到iframe，再切换到iframe
iframe = web.find_elements(by=by.By.XPATH, value='xxxxxx')
web.switch_to.frame(iframe)  # 切换到iframe
web.switch_to.default_content()  # 默认的窗口，一般是上一个窗口（切换回去）


