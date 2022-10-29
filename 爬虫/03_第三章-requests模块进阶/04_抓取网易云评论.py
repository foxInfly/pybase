"""
1.找到加密的参数  # window.arsea(参数)
     window.asrsea = d,
     window.ecnonasr = e
     # 生成指定a个的随机数字
     function a(a) {  # a=16
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)
            e = Math.random() * b.length,
            e = Math.floor(e),
            c += b.charAt(e);
        return c
    }
    # a = 要加密的数据，如入参的json字符串
    # b = 秘钥，如"0CoJUm6Qyw8W8jud"，或者随机字符串
    function b(a, b) {
        var c = CryptoJS.enc.Utf8.parse(b)  #转成urf8，其实就是加密的秘钥
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a)   #入参
          , f = CryptoJS.AES.encrypt(e, c, {   #AES加密
            iv: d, #偏移量
            mode: CryptoJS.mode.CBC  # 机密模式CBC
        });
        return f.toString()
    }
    #a 是指定个数的随机数
    #b、c都是取的配置好的数据
    function c(a, b, c) {
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    }

    function d(d, e, f, g) {   #参数中d:入参的json字符串，e是个固定值，当前 "流泪": "01000",
        var h = {}   #空对象
          , i = a(16); #调用a(方法) 生成16位的随机数
        # 下面这种写法，其实就是return的最后的h，执行完上面的三句代码
        return h.encText = b(d, g), # 调用b()方法，结果赋值给h.encText
        h.encText = b(h.encText, i),
        h.encSecKey = c(i, e, f), 调用c()方法，结果赋值给h.encSecKey
        h
    }
    function e(a, b, d, e) {
        var f = {};
        return f.encText = c(a + e, b, d),
        f
    }
2.想办法进行加密（参考网易的逻辑）params==>encText encSecKey==>encSecKey
3.拿到数据


"""
import requests

url = "https://music.163.com/weapi/comment/resource/comments/get?csrf_token="
# 真是参数
params = {
    "csrf_token": "",
    "cursor": "-1",
    "offset": "0",
    "orderType": "1",
    "pageNo": "1",
    "pageSize": "20",
    "rid": "A_PL_0_596729952",
    "threadId": "A_PL_0_596729952"
}
e = "01000"
f = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56" \
    "135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97d" \
    "def52741d546b8e289dc6935b3ece0462db0a22b8e7 "
g = "0CoJUm6Qyw8W8jud" # 秘钥
i = "dDRmsKkCHH9NK0dd"  # 随机的字符串


def get_encText() -> str:
    return "1BdkwtG7WE0mHUqNi8wmL2Xf05m9FThHCjdMIFXTYMtu3VkBqiwon+ceNf7CLeRPaEex5eQufOm8HpFD5FJTuDgtYYWtQF3m56AUy8R03XPrd2fvcYDzhUvv0xf9+X0N"


def get_encSecKey() -> str:
    return "7682f4e9725c72feba4fc68affe0af95feb44fe17f5720b216e9a3e2159cd0c1bcaac4f380eb6641d842c719c97ab3d28d541d7001affa38a3bd2afd5b8eb9abfe4cffe61586f8f6d07899a03fdacba11129acf45e4ebc72c6bba1a4027f72c62a78d292c9e7f0f0ffc55d97874f4d9315a4dd4a0e932e440c406b8aab0a4962"


def get_Params(data):
    first = enc_params(data, g)
    pass


def enc_params(data, key):  # 加密过程
   pass

