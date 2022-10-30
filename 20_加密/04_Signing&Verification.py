"""
数字签名：证明发布者是真的发布者
digital signature:
    1.signing
        plain_txt --(hash)--> hashKey --(private key)--> digital signature(signed mesage)
    2.verification
        1. input msg --(hash)--> hashKey
        2. digital signature  --(public key)--> calculations 得到一个值，这个值是发送者的hash值
        3. 比较两个hashKey是否一样，就是校验
证书：公钥的分发
certificate：签发证书的的机构certificate authority（CA），经由它签发的“文件”，我们称之为certificate证书
证书其实是一种特殊的签名
证书内容：
    1.拥有者的信息（https证书的话，包含域名、公司组织、地点等）
    2.证书颁发者的信息
    3.证书拥有者的公钥
    4.对公钥和其他信息的签名
https://note.youdao.com/web/#/file/WEBc8b9e5d445b7f95ccbfbd20e85331dc8/note/WEBf4c9ea4f9a0ff5441d27bccbbe89aede/
"""