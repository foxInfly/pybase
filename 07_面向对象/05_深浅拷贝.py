"""
变量的赋值：
    只是形成两个变量，实际上还是指向同一个对象
浅拷贝：
    python一般都是浅拷贝，拷贝时，对象的子对象内容不拷贝，因此源对象与拷贝对象会引用同一个对象
深拷贝：
    使用copy模块的deepcopy函数，递归拷贝对象中包含的子对象，源对象和拷贝对象所有的子对象也不相同

"""

import copy

copy.copy()
copy.deepcopy()

