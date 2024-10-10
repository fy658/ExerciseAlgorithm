"""
问题描述
给定一个正整数数组 ，数组最大长度为 100。你需要从第一个元素开始，计算到达数组最后一个元素所需的最少步数。

移动规则如下：

第一步必须从第一个元素开始，步长范围为 ，其中[1,len/2]   len为数组长度。   #数组是从0开始
从第二步开始，每一步的步长必须等于当前所在位置的元素值，不能多也不能少。
只能向数组尾部移动，不能往回走。
如果无法到达最后一个元素，则返回 。

输入格式
输入为一行，包含若干个正整数，以空格分隔，表示给定的数组 。数组长度小于 100。

输出格式
输出一个整数，表示最少的步数。如果无法到达最后一个元素，输出 。

样例输入1
7 5 9 4 2 6 8 3 5 4 3 9
样例输出1
2
"""

array_list = list(map(int, input().split()))
#设置一个数组，每个元素的值表示到达输入数组每个元素需要的最小步数，初始都设为无穷大
dp_arr = [float('inf')]*len(array_list)
dp_arr[0]=0
for i in range(1, len(array_list)//2):
    dp_arr[i] = 1
for j in range(len(array_list)):
    if dp_arr[j] != float('inf'):
        next_index = j+array_list[j]
        if next_index<len(array_list):
            dp_arr[next_index] = dp_arr[j]+1
if dp_arr[-1]!=float('inf'):
    print(dp_arr[-1])
else:
    print(-1)