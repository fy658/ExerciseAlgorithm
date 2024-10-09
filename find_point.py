"""
题目描述
公司组织了一次考试,现在考试结果出来了，想看一下有没人存在作弊行为,但是员工太多了,需要先对员工进行一次过滤,再进一步确定是否存在作弊行为。

过滤的规则为:找到分差最小的员工ID对(p1,p2)列表,要求p1<p2

员工个数取值范国:O<n<100000

员工ID为整数,取值范围:0<=n<=100000

考试成绩为整数,取值范围:0<=score<=300

输入描述
员工的ID及考试分数

输出描述
分差最小的员工ID对(p1,p2)列表,要求p1<p2。每一行代表一个集合,每个集合内的员工ID按顺序排列,多行结果也以员工对中p1值大小升序排列(如果p1相同则p2升序)。

样例1
输入：

5
1 90
2 91
3 95
4 96
5 100
输出:

1 2
3 4


数组存贮元祖，元祖包含id,point
3
1 30
2 31
3 50
[(1, 30), (2, 31), (3, 50)]
"""

num = int(input())
emp_info = []
# 无穷大的数表示
min_minus = float('inf')
res = []
for _ in range(num):
    id, point = map(int, input().split())
    emp_info.append((id, point))
emp_info.sort(key=lambda x: x[1])
print(emp_info)
for index in range(1, num):
    diff_point = emp_info[index][1] - emp_info[index-1][1]
    if diff_point< min_minus:
        min_minus = diff_point
        res = [(emp_info[index-1][0], emp_info[index][0])]
        print("$$$$", res)
    elif diff_point==min_minus:
        res.append((emp_info[index-1][0], emp_info[index][0]))
        print("@@@@", res)
res.sort()
print("#####",res)
for item in res:
    print(item[0], item[1])



