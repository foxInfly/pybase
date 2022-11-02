"""
Flask 是一个使用 Python 编写的轻量级 Web 应用程序框架。Armin Ronacher带领一个名为Pocco的国际Python爱好者团队开发了Flask。
Flask基于Werkzeug WSGI工具包和Jinja2模板引擎。两者都是Pocco项目
Web Server Gateway Interface（Web服务器网关接口，WSGI）,WSGI是Web服务器和Web应用程序之间通用接口的规范。
Werkzeug 它是一个WSGI工具包，它实现了请求，响应对象和实用函数，Flask框架使用Werkzeug作为其基础之一。
jinja2是Python的一个流行的模板引擎。Web模板系统将模板与特定数据源组合以呈现动态网页。


1.安装
    pip install flask -i https://pypi.tuna.tsinghua.edu.cn/simple
        Flask-2.2.2-py3-none-any.whl(101 kB)
        click-8.1.3-py3-none-any.whl(96 kB)
        importlib_metadata-5.0.0-py3-none-any.whl (21 kB)
        itsdangerous-2.1.2-py3-none-any.whl (15 kB)
        Werkzeug-2.2.2-py3-none-any.whl (232 kB)
        Jinja2-3.1.2-py3-none-any.whl (133 kB)
        colorama-0.4.6-py2.py3-none-any.whl (25 kB)
        zipp-3.10.0-py3-none-any.whl(6.2 kB)
        MarkupSafe-2.1.1-cp38-cp38-win_amd64.whl (17 kB)
    pip install pandas -i https://pypi.tuna.tsinghua.edu.cn/simple
        pandas-1.5.1-cp38-cp38-win_amd64.whl (11.0 MB)
        numpy-1.23.4-cp38-cp38-win_amd64.whl (14.7 MB)
        pytz-2022.6-py2.py3-none-any.whl (498 kB)
        python_dateutil-2.8.2-py2.py3-none-any.whl (247 kB)
        six-1.16.0-py2.py3-none-any.whl (11 kB)

"""
from flask import Flask, render_template, request
import pandas as pd

# 创建web应用后
app = Flask(__name__)


@app.route("/hello")  # 访问的路由
def helloWorld():
    return "hello World"


@app.route("/login", methods=["post"])  # 访问的路由
def login():
    dic = request.form
    print(dic)
    print(dic.get("username"))
    print(dic.get("password"))
    return "成功"


@app.route("/")  # 访问的路由
def index():
    name_str = "lp"
    lst = ["ss", "mumu", "22"]
    data = pd.read_csv("data.csv")
    data = data.rename(columns={"3": "name", "2": "value"})
    print(data)
    data = data.to_dict(orient="records")
    print(data)
    # name_str会传给页面中的name变量
    return render_template("hello.html", name=name_str, lst=lst, data =data)  # 默认去./templates下找对应的文件并返回


if __name__ == '__main__':
    # app.run()  # 启动应用程序
    app.run(debug=True)  # 默认会重启服务器
