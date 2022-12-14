"""
优点：速度快，效率高，准确性高
缺点：上手有难度

规则：使用元字符进行排列组合来匹配字符    https://tool.oschina.net/regex

元字符：具有固定含义的特殊字符
常用元字符：
    .   匹配除换行符以外的任意字符
    \w  匹配字母或数组或下划线  word
    \s  匹配任意的空白符   space
    \d  匹配数字 digit
    \n  匹配一个换行符  enter
    \t  匹配一个制表符   Tab

    ^  匹配字符串的开始
    $  匹配字符串的结束

    \W  匹配非字母非数字非下划线   \s的反面
    \D  匹配非数字
    \S  匹配非空白
    a|b 匹配字符a或b
    ()  匹配括号内的表达式，也可能是一个数组
    [...]   匹配字符组中的字符
    [^...]  匹配除了字符组中字符的所有字符

量词：控制页面的元字符出现的次数
    *  重复0次或多次
    +  重复1次或多次
    ?  重复0次或1次
    {n}   重复n次
    {n,}  重复n次及以上
    {n,m} 重复n到m次

贪婪匹配和惰性匹配
    .*  贪婪匹配   可以匹配很多意思
    .*? 惰性匹配  0-1次把*变少  a.*?b  如assbsswwbaaab   匹配出assb；原理是先.*；然后再往回找，最少的
            用途，<div>.*?</div>
"""
