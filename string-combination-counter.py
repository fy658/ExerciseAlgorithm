"""
题目描述：构成指定长度字符串的个数
给定 M（0 < M ≤ 30）个字符（a-z），从中取出任意字符（每个字符只能用一次）拼接成长度为 N（0 < N ≤ 5）的字符串，

要求相同的字符不能相邻，计算出给定的字符列表能拼接出多少种满足条件的字符串，

输入非法或者无法拼接出满足条件的字符串则返回0。

输入描述
给定的字符列表和结果字符串长度，中间使用空格(" ")拼接

输出描述
满足条件的字符串个数

用例1
输入

aab 2

输出

2

说明

只能构成ab,ba。

用例2
输入

abc 2

输出

6

说明

可以构成：ab ac ba bc ca cb 。

"""


def generate_diff_string(s, length, curr, res, used):
    print("curr=", curr, used)
    if len(curr) == length:
        res.add(curr)
        print("res", res)
        return

    for i in range(len(s)):
        print("loop", i)
        if used[i] or (len(curr)>0 and curr[-1]==s[i]):
            continue
        used[i] = True
        generate_diff_string(s, length, curr+s[i], res, used)
        print(curr+s[i])
        used[i] = False
        print(used)


def count_valid_strings(s, lenth):
    used = [False]*len(s)
    distinct_str = set()
    generate_diff_string(s,lenth, "", distinct_str, used)
    print("####", distinct_str)
    return len(distinct_str)








# 读取输入
input_str = input().strip()
try:
    chars, length = input_str.split()
    length = int(length)
except ValueError:
    print(0)
    exit()

# 计算并输出结果
count_valid_strings(chars, length)


"""

"""