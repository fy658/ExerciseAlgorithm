"""
华为机试  2024/10/16 E卷   成语接龙

输入
5
1
add
da
pay
doo
opp
输出
adddoo
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