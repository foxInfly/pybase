"""
pip install cryptography -i https://pypi.tuna.tsinghua.edu.cn/simple
    cryptography-38.0.1-cp36-abi3-win_amd64.whl (2.4 MB)
    cffi-1.15.1-cp38-cp38-win_amd64.whl (178 kB)
    pycparser-2.21-py2.py3-none-any.whl (118 kB)


"""

from cryptography.fernet import Fernet
import hashlib

print(__name__)
def encrypt(key, plain_txt):
    f = Fernet(key)
    return f.encrypt(plain_txt)


def decrypt(key, cipher):
    f = Fernet(key)
    return f.decrypt(cipher)


"""
一个python的文件有两种使用的方法，
    第一是直接作为脚本执行，(这时内置变量__name__ == "__main__")
    第二是import到其他的python脚本中被调用（模块重用）执行。
因此if __name__ == 'main': 的作用就是控制这两种情况执行代码的过程，
在if __name__ == 'main': 下的代码只有在第一种情况下（即文件作为脚本直接执行）才会被执行，而import到其他脚本中是不会被执行的。
原理：
    每个python模块（python文件，xx.py）都包含内置的变量__name__,当运行模块被执行的时候，__name__等于文件名（包含了后缀.py）
    如果import到其他模块中，则__name__等于模块名称（不包含后缀.py）
"""
if __name__ == "__main__":
    key = Fernet.generate_key()  # 一般自己生成，易于记住
    print(f"key={key}")
    cipher_txt = encrypt(key=key, plain_txt=b"attack")
    print(cipher_txt)
    plain_txt = decrypt(key=key, cipher=cipher_txt)
    print(plain_txt)
    print(hashlib.sha256(b"lp").hexdigest())  # hash一般会加盐，如密码
