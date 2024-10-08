"""
题目描述
众数是指一组数据中出现次数量多的那个数，众数可以是多个。

中位数是指把一组数据从小到大排列，最中间的那个数，如果这组数据的个数是奇数，那最中间那个就是中位数，如果这组数据的个数为偶数，那就把中间的两个数之和除以2，所得的结果就是中位数。

查找整型数组中元素的众数并组成一个新的数组，求新数组的中位数。

输入描述
输入一个一维整型数组，数组大小取值范围 0<N<1000，数组中每个元素取值范围 0<E<1000

输出描述
输出众数组成的新数组的中位数

"""

input_num = input()
input_list = list(map(int, input_num.split()))
stat_num = {}
for item in input_list:
    if item in stat_num:
        stat_num[item]+=1
    else:
        stat_num[item]=1
max_count = max(stat_num.values())
max_number = [num for num, val in stat_num.items() if val==max_count]
print(max_number)

