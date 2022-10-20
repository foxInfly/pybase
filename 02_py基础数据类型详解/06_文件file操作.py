"""
1. 打开文件
open(路径,操作模式mode,编码encoding)
    路径：绝对路径（从根目录出发）；相对路径（相对当前目录）
    mode:缺省；  r=read  w=write  a=append b=binary(二进制非文本文件)
    encoding:缺省
with()打开的文件，会自动管理连接
"""
# 读
# f = open("../source/note.txt", mode="r", encoding="utf-8")  # 打开文件，并还没有加载到内存
# content = f.read()  # 全部读取
# content = f.readline()  # 读取一行
# content = f.readline().strip()  # 读取一行,同时去除两边空白字符（空格、换行、制表符等）
# content = f.readlines()  # 按行读取到一个列表中  读完会自动关闭管道，
# print(content)

# f = open("../source/note.txt", mode="r", encoding="utf-8")  # 需要再次打开
# for line in f:
#     print(line.strip())

# 写
# f = open("../source/note2.txt", mode="w", encoding="utf-8")   # 没有创建，有则清空文件
# f = open("../source/note2.txt", mode="a", encoding="utf-8")   # 没有创建，有则在后面追加内容
# f.write("1. 李普 apc")
# f.close()   # 关闭连接

# with代码块结束，会关闭连接
# with open("../source/note2.txt", mode="a", encoding="utf-8") as f:
#     f.write("1. 李普 apc")

# 读取非文本文件是，要加b，就是二进制的意思，不要给encoding
with open("../source/11.png", mode="rb") as f1,  open("../source/12.png", mode="wb") as f2:
    for line in f1:
        f2.write(line)
