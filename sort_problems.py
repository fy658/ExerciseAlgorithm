def bubble_sort(lists):
    # i 可以写len(lists)， 也可以写len(lists)-1, 因为i = 0 一直到 i=len(lists)时，最后一次j=(0, len(lists)-(len(lists)-1)-1)
    # 也就是j= (0,0),没有元素比较，所以直接写成 for i in range(len(lists)-1)
    for i in range(len(lists)-1):
        # 进行一轮比较换位后，n个元素中的最大元素将位于第n位，然后对前n-1个元素进行第二轮比较，重复该过程直到进行比较的元素只剩下一个为止
        # len(lists)-i-1是为了防止数组out of index，j=(0,len(lists)-i-1)表示比较了len(lists)-i-1次
        for j in range(len(lists)-i-1):
            if lists[j]>lists[j+1]:
                lists[j], lists[j+1] = lists[j+1], lists[j]
        print(f"比较了{len(lists)-i-1}次", lists)
    return lists

print(bubble_sort([36,25,48,12,26,65,43,57]))


"""
模拟排序

高矮个子排队
问题描述
有一队小朋友站成一排，他们的身高各不相同。我们用一个正整数数组来表示这队小朋友的身高，例如 {5,3,1,2,3}。

现在我们希望将这些小朋友重新排队，使他们按照"高""矮""高""矮"的顺序排列。具体要求如下：

每个"高"位置的小朋友要比相邻位置的小朋友高或者一样高。
每个"矮"位置的小朋友要比相邻位置的小朋友矮或者一样矮。
小朋友们移动的总距离要最小。
排队从"高"位置开始。
例如，对于小队 {5,3,1,2,3}，一个满足条件的排序结果是 {5,1,3,2,3}。

注意，虽然 {5,2,3,1,3} 也满足"高""矮""高""矮"的顺序，但小朋友们的移动距离较大，所以不是最优结果。

移动距离的定义如下：

如果一个小朋友从第二位移到第三位，移动距离为 。
如果移动到第四位，移动距离为 ，以此类推。
输入格式
输入为一行，包含若干个用空格分隔的正整数，表示小朋友们的身高。

输出格式
输出为一行，包含若干个用空格分隔的正整数，表示重新排序后小朋友们的身高。

样例输入1
4 1 3 5 2
样例输出1
4 1 5 2 3
样例输入2
1 1 1 1 1
样例输出2
1 1 1 1 1
样例输入3
xxx
样例输出3
[]
"""

"""
这道题目要求我们将一队小朋友按照"高""矮""高""矮"的顺序重新排列，同时要求移动距离最小。解题的关键在于理解题目要求和找到一个高效的排序方法。

首先，我们需要明白"高""矮"交替的含义：

奇数位置（第1、3、5...位）的小朋友应该比相邻的小朋友高或相等。
偶数位置（第2、4、6...位）的小朋友应该比相邻的小朋友矮或相等。
解决这个问题的一个有效方法是使用冒泡排序的思想，但我们只需要进行一次遍历：

从左到右遍历数组。
对于奇数位置，如果当前小朋友比右边的矮，就交换它们。
对于偶数位置，如果当前小朋友比右边的高，就交换它们。
这个方法之所以有效，是因为：

它保证了奇数位置的小朋友总是不低于偶数位置的小朋友。
每次交换都是相邻位置的交换，保证了移动距离最小。
一次遍历就能完成排序，因为我们只需要保证相邻位置的大小关系正确。
时间复杂度分析：

算法只需要遍历一次数组，所以时间复杂度是O(N) ，其中 N 是小朋友的数量。
对于给定的数据范围（N<100），这个复杂度是完全可以接受的。
需要注意的是，我们还需要处理输入可能非法的情况，比如输入不是数字时，应该返回空数组。

这个解法的优点是简单直观，容易实现，而且能够保证最小的移动距离。
"""


def arrange_queue(array_input):
    length = len(array_input)
    # 再次检查输入是否合法
    if not all(isinstance(h, int) and h>0 for h in array_input):
        return("[]")
    if length == 1:
        return " ".join(list(map(str, array_input)))
    for i in range(length-1):
        if i%2==0:
            if array_input[i]<array_input[i+1]:
                array_input[i] , array_input[i + 1] = array_input[i+1], array_input[i]
        if i%2!=0:
            if array_input[i]>array_input[i+1]:
                array_input[i], array_input[i + 1] = array_input[i + 1], array_input[i]
    return " ".join(list(map(str, array_input)))

# 处理输入异常

try:
    inputs = input()
    input_list = list(map(int, inputs.split()))
    print(arrange_queue(input_list))
except:
    print("[]")
