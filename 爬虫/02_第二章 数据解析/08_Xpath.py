"""
Xpath是在XML中搜索内容的一门语言
    类似正则，比正则更简单；html是xml的子集
需要安装：
    pip install -i https://pypi.tuna.tsinghua.edu.cn/simple lxml
        lxml-4.9.1-cp38-cp38-win_amd64.whl
"""

from lxml import etree
import requests

xml = """
<book>
    <id>1</id>
    <name>野花遍地香</name>
    <price>1.23</price>
    <nick>臭豆腐</nick>
    <author>
        <nick id="10086">李普</nick>
        <nick id="10010">沐沐</nick>
        <nick class="joy">琼</nick>
        <nick class="joly">林</nick>
        <span>
            <nick>hua</nick>
        </span>
        <div>
            <nick>水</nick>
        </div>
    </author>
    <pattern>
        <nick id="pp">匹配</nick>
        <nick id="ll">来了</nick>
    </pattern>
</book>

"""
tree = etree.XML(xml)  # 把xml封装成etree对象
print(type(etree))
# result = tree.xpath("/book")  # 找根节点
# result = tree.xpath("/book/name")  # 找name节点
# result = tree.xpath("/book/name/text()")  # 找name节点的文本
# result = tree.xpath("/book/author/nick/text()")  # 找name节点的文本
# result = tree.xpath("/book/author//nick/text()")  # //找后代里面匹配的（含当前）
result = tree.xpath("/book/author/*/nick/text()")  # //*是通配符，任意的节点（不含当前）
print(result)

tree2 = etree.parse("a.html")  # 把xml封装成etree对象
# result2 = tree2.xpath("/html/body/ul/li/a/text()")
# result2 = tree2.xpath("/html/body/ul/li[1]/a/text()")  # 从1开始数数 []表示索引
# result2 = tree2.xpath("/html/body/ol/li/a[@href='dapao']/text()")  # 从1开始数数 [@href='dapao']属性筛选
result2 = tree2.xpath("/html/body/ol/li")
for li in result2:
    # re = li.xpath("./a/text()")   # 相对路径
    re = li.xpath("./a[@href]/text()")   # 拿属性的值
    print(re)
print(tree2.xpath("/html/body/ul/li/a/@href"))

url3 = "https://hefei.zbj.com/search/service/?kw=saas&r=1&nt=3606&fcn=%E7%94%B5%E5%AD%90%E5%95%86%E5%9F%8E%E7%B3%BB%E7%BB%9F"
resp3 = requests.get(url3)
print(resp3.text)

