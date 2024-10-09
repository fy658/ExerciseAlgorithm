"""
描述
给定两个字符串 S 和 T ，判断 S 是否是 T 的子序列。
即是否可以从 T 删除一些字符转换成 S。
保证字符串中仅含有小写字母
示例1
输入：
"nowcoder","nowcoder"
复制
返回值：
true
"""
from re import U


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param S string字符串
# @param T string字符串
# @return bool布尔型
#
class Solution:
    def isSubsequence(self, S: str, T: str) -> bool:
        # write code here
        if S == T:
            return True
        i = 0
        j = 0
        while i < len(S) and j < len(T):
            if S[i] == T[j]:
                i += 1
                j += 1
            else:
                j += 1

        if i == len(S):
            return True
        else:
            return False



"""
最长的指定瑕疵度的元音子串
"""

input_1 = int(input())
input_2 = input()

special_str = ['a', 'o', 'e', 'i', 'u', 'A', 'O', 'E', 'I', 'U']

# 找到所有输入字符串的元音字母的索引
index_of_str = [index for index in range(len(input_2)) if input_2[index] in special_str]
print(index_of_str)
l_index=0
r_index=0
res = []
while r_index<len(index_of_str):
    # 计算当前子串的瑕疵度
    num = index_of_str[r_index] - index_of_str[l_index]-(r_index-l_index)
    # 等于瑕疵度
    if num== input_1:
        res.append(index_of_str[r_index]-index_of_str[l_index]+1)
        r_index+=1
    #小于瑕疵度
    elif num<input_1:
        r_index+=1
    # 大于瑕疵度
    else:
        l_index+=1
if not res:
    print(0)
print(res)
print(max(res))


