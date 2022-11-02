"""
目的是拿数据，不需要打开浏览器，后台默默运行就好，就是无头浏览器

"""
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import by
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time


# 转备好参数配置(无头浏览器，速度其实没有快多少)
opt = Options()
opt.add_argument("--headless")  # 无头
opt.add_argument("--disable-gpu")  # 不显示

web = Chrome(options=opt)
# web = Chrome(chrome_options=opt)
# 2.用浏览器打开url;必须写全，包含https://
web.get("https://www.endata.com.cn/")

'''
# 定位下拉列表
select_el = web.find_element(by=by.By.XPATH, value='xxxxxx')
sel = Select(select_el)  # 封装成Select对象
# sel.options # select的所有选项option
for i in range(len(sel.options)):
    sel.select_by_index(i)  # 根据索引进行切换
    time.sleep(2)
'''

# 拿取加载后的源代码elements
print(web.page_source)
