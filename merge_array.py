"""
问题描述
现在有多组整数数组，需要将它们合并成一个新的数组。合并规则如下：从每个数组里按顺序取出固定长度的内容合并到新的数组中，取完的内容会删除掉。如果该行不足固定长度或者已经为空，则直接取出剩余部分的内容放到新的数组中，继续下一行。

输入格式
第一行是每次读取的固定长度 ，满足 。

第二行是整数数组的数目 ，满足 。

第  到第  行是需要合并的数组，不同的数组用回车换行分隔，数组内部用逗号分隔，每个数组最多不超过  个元素。

输出格式
输出一个新的数组，用逗号分隔。

样例输入1
3
2
2,5,6,7,9,5,7
1,7,4,3,4

样例输出1
2,5,6,1,7,4,7,9,5,3,4,7

样例输入2
4
3
1,2,3,4,5,6
1,2,3
1,2,3,4
样例输出2
1,2,3,4,1,2,3,1,2,3,4,5,6

样例输入3
3
2
2,5,6,7,,,9,5,7
1,7,4,3,,4
样例输出3
2,5,6,1,7,4,7,9,5,3,4,7
"""

get_num = int(input())
array_num = int(input())
array = [list(filter(lambda x: x != '', input().split(','))) for _ in range(array_num)]
print(array)
new_array = []
i=0
max_length = max(list(map(len, array)))
while i<max_length:
        for arr in range(array_num):
                new_array.extend(array[arr][i:i+get_num])
        i+=get_num
print(','.join(new_array))