"""
Cryptography、Cryptology都可以翻译成密码学；Cryptography倾向于机密技术的应用，后者倾向于密码技术的研究；
    作为程序员，接触最多的是Cryptography，不管SSL还是HTTPS，都是加密技术的应用

 Plaintext: 未经加密额消息，任何人都可以读
Ciphertext: 加密的信息，未解密前，不可读
       key: 秘钥（加解密使用，核心是算法）

plaintext   --(encryption)-->  ciphertext  --(decryption)-->  plaintext
加密的种类：
    对称加密：Symmetric Cryptography,  可以使用相同的key进行加解密,如：DES、3DES、AES、RC4、RC5、RC6
        plaintext   --(secret key)-->  ciphertext  --(secret key)-->  plaintext
    非称加密：Asymmetric Cryptography,  可以使用相同的key进行加解密，如：RSA、DSA（数字签名用）、ECC（移动设备用）、Diffie-Hellman
         plaintext   --(public key)-->  ciphertext  --(secret key)-->  plaintext
    散列（hash）：MD2、MD4、MD5、SHA、SHA-1

Advanced Encryption Standard，AES；用来替代原先的DES（Data Encryption Standard）
MD5 Message-Digest Algorithm 5；更好的SHA-2（Secure Hash Algorithm 2）
RSA是1977年由罗纳德·李维斯特（Ron Rivest）、阿迪·萨莫尔（Adi Shamir）和伦纳德·阿德曼（Leonard Adleman）一起提出。
当时他们三人都在麻省理工学院工作。RSA就是他们三人姓氏开头字母拼在一起组成的。public key和加解密算法都公开，但私钥不公开（用户持有）；
    根据数论(number theory,数字理论，主要研究整数理论的学科)，寻求两个大素数比较简单，而将它们的乘积进行因式分解却极其困难，
    因此可以将乘积公开作为加密密钥



"""