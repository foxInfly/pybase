"""
1. 字符集合编码
   字符集，就是不同的文字对应的人禁止是什么样的
   ascii  1个byte,128个文字字符
   ANSI   2个byte，16bit;  65535个
       ANSI-GB2312，升级成gbk（windows默认）,..还是不够用
       ANSI-big5
       ANSI-JIS
   Unicode
     早期UCS-2   2个字节 不够用
     UCS-4    固定4个字节（没法用，只是一个标准）
   utf: 可变长度的Unicode
   utf-8 常见（Mac默认编码）   最短的字节长度8bite   英文8bite 欧洲文字16bit  中文3bit（一千六百多万）；gbk占的资源少
   utf-16 少见   最短的字节长度16bite
  gbk不能直接和utf-8转换；只能通过源文件，翻译后再编码（间接转）

2. bytes


"""
s = "李普"
print(s.encode("gbk"))  # 使用gbk编码 b'xxxx'是bytes类型的数据 4ge\x  代表两个汉字； b'\xc0\xee\xc6\xd5'
print(s.encode("utf-8"))  # 使用utf-8编码 b'xxxx'是bytes类型的数据 6ge\x  代表两个汉字
bs = b'\xc0\xee\xc6\xd5'
bs2 = b'\xe6\x9d\x8e\xe6\x99\xae'
print(bs.decode("gbk"))  # 解码
print(bs.decode("gbk").encode("utf-8"))  # 解码再编码

"""
1. 算术运算 + - * / % //(整除)
2. 比较运算 == !=  > < >= <=
3. 赋值运算 = += -= *=
4. 逻辑运算 and  or  not  优先级：括号 > not > and > or  最好价格括号，好读
5. 成员运算 in    not in
"""
