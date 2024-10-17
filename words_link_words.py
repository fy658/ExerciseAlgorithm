"""
华为机试  2024/10/16 E卷   成语接龙

题目描述

单词接龙的规则是：可用于接龙的单词首字母必须要前一个单词的尾字母相同；当存在多个首字母相同的单词时，取长度最长的单词，如果长度也相等，则取字典序最小的单词；已经参与接龙的单词不能重复使用。现给定一组全部由小写字母组成单词数组，并指定其中的一个单词作为起始单词，进行单词接龙，请输出最长的单词串，单词串是单词拼接而成，中间没有空格。

输入描述

输入的第一行为一个非负整数，表示起始单词在数组中的索引K，0 <= K < N ；

输入的第二行为一个非负整数，表示单词的个数N；

接下来的N行，分别表示单词数组中的单词。

输出描述

输出一个字符串，表示最终拼接的单词串。

补充说明

单词个数N的取值范围为[1, 20]；

单个单词的长度的取值范围为[1, 30]；

用例1

输入

0

6

word

dd

da

dc

dword

d

输出

worddwordda

说明：先确定起始单词word，再接以d开头的且长度最长的单词dword，剩余以d开头且长度最长的有dd，da，dc，则取字典序最小的da，所以最后输出worddwordda。

用例2

输入

4

6

word

dd

da

dc

dword

d

输出

dwordda

说明：先确定起始单词word，剩余以d开头且长度最长的有dd，da，dc，则取字典序最小的da,所以最后输出dwordda。
"""

num = int(input())
start_index = int(input())
list_words = [str(input()) for _ in range(num)]


def get_link_words(arr, start_word):
    global result
    collect_word = []
    for item in arr:
        if item[0]== start_word[-1]:
            collect_word.append(item)
    if len(collect_word)>0:
        link_word = sorted(collect_word, key=len, reverse=True)[0]
        start_word+=link_word
        get_link_words(arr, start_word)

    else:
        result = start_word


result = ""
res = get_link_words(list_words, list_words[start_index-1])
print("###", result)


"""
打卡，输入数字num代表学生记录数，后面是num个学生的打卡记录，请输入打卡异常的记录
"""


"""
分词
"""