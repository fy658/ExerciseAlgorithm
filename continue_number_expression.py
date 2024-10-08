"""
问题描述
给定一个正整数
𝑇，请找出所有用连续自然数之和来表示
𝑇的方案。例如，整数
9 可以表示为：
9=9，
9=4+5，
9=2+3+4。你的任务是按照以下要求，输出所有表示
𝑇的方案：

优先输出自然数个数最少的表达式。
每个表达式中的自然数按照递增顺序输出。
最后输出表达式的总数。
输入格式
输入一个正整数
𝑇。

输出格式
按照题目要求，输出所有表示
𝑇的方案，每个方案占一行。最后一行输出 Result:X，其中
𝑋表示方案总数。

样例输入1
9
样例输出1
9=9
9=4+5
9=2+3+4
Result:3
样例输入2
10

"""
target = int(input())
print(target,"=",target, sep="")
result = []
for i in range(1, target):
    # sum和express放在每一个循环后面使得每一个枚举得到一个sum和表达式
    sum = 0
    express = ""
    for j in range(i, target):
        sum += j
        express = express + str(j)+"+"
        if sum==target:
            result.append(str(target)+"=" +express[:-1])
            break
result.sort(key=lambda x: len(x))
for res in result:
    print(res)


"""
双指针滑动窗口解法
"""
array = [i+1 for i in range(target)]

left, right, total = 0, 1, array[0]
res = []
while left<target:
    if total>target:
        total-=array[left]
        left+=1
    elif total==target:
        res.append(array[left:right])
        total -= array[left]
        left += 1
        if right >= target:
            break
        else:
            total += array[right]
            right += 1
    else:
        total += array[right]
        right += 1

res.sort(key=lambda x: len(x))
for item in res:
    print(f"{target}={'+'.join(map(str, item))}")









