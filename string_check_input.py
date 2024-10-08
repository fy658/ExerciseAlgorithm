"""
题目描述
给定用户密码输入流 input，输入流中字符 '<' 表示退格，可以清除前一个输入的字符，请你编写程序，输出最终得到的密码字符，并判断密码是否满足如下的密码安全要求。

密码安全要求如下：

密码长度 ≥ 8；
密码至少需要包含 1 个大写字母；
密码至少需要包含 1 个小写字母；
密码至少需要包含 1 个数字；
密码至少需要包含 1 个字母和数字以外的非空白特殊字符；
注意空串退格后仍然为空串，且用户输入的字符串不包含 '<' 字符和空白字符。

输入描述
用一行字符串表示输入的用户数据，输入的字符串中 '<' 字符标识退格，用户输入的字符串不包含空白字符，例如：

ABC<c89%000<

输出描述
输出经过程序处理后，输出的实际密码字符串，并输出改密码字符串是否满足密码安全要求。两者间由 ',' 分隔， 例如：

ABc89%00,true

"""

"""
Python的字符串对象有很多内置的方法。让我为您列举一些最常用和最重要的字符串方法。
以下是Python字符串的一些常用方法：

lower(): 将字符串转换为小写。
upper(): 将字符串转换为大写。
strip(): 删除字符串两端的空白字符（或指定字符）。
lstrip(): 删除字符串左侧的空白字符（或指定字符）。
rstrip(): 删除字符串右侧的空白字符（或指定字符）。
split(): 按指定分隔符分割字符串为列表。
join(): 将可迭代对象中的字符串连接起来。
replace(): 替换字符串中的子串。
startswith(): 检查字符串是否以指定子串开头。
endswith(): 检查字符串是否以指定子串结尾。
find(): 查找子串，返回最左边的索引，如果找不到返回-1。
rfind(): 从右侧开始查找子串。
index(): 类似find()，但如果找不到子串会抛出ValueError。
count(): 计算子串在字符串中出现的次数。
isalpha(): 检查字符串是否全部由字母组成。
isdigit(): 检查字符串是否全部由数字组成。
isalnum(): 检查字符串是否由字母和数字组成。
capitalize(): 将字符串的第一个字符转换为大写。
title(): 将字符串中每个单词的首字母转换为大写。
swapcase(): 将字符串中的大小写字母互换。
"""


input_str = input()
res = ""
for s in input_str:
    if s=="<":
        res = res[:-1]
    else:
        res+=s
is_digit = False
is_lower = False
is_upper = False
is_spec = False
print(res)
for ch in res:
    if ch.isdigit():
        is_digit = True
    elif ch.isupper():
        is_upper = True
    elif ch.islower():
        is_lower = True
    else:
        is_spec = True
flag_res = len(res)>=8 and is_digit and is_upper and is_lower and is_spec
print(res+","+str(flag_res).lower())
