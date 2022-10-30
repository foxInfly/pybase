"""
linux
    生成私钥：
        openssl genrsa -out provate.pem    默认是2048
        openssl genrsa -out provate.pem 3072
    根据私钥生成公钥
        openssl rsa -in provate.pem -pubout > public.pem
    查看私钥的参数：
        openssl rsa -in provate.pem -text -noout
    查看公钥的参数：
        openssl rsa -pubin -in public.pem -noout -modulus

"""


