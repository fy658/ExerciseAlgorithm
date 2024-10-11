"""
第k个排列
给定参数n 从1到n会有n个整数 1，2，3，…n 这n个数字共有n!种排列 按大小顺序升序列出所有排列情况 并一一标记
当n=3时，所有排列如下 “123”,“132”,“213”,“231”,“312”,“321” 给定n和k 返回第n个排列
输入格式
第一行包含两个正整数 n 和 k,表示给定的参数。

输出格式
输出排在第 k 位置的数字。

样例输入1
3 3
样例输出1
213
样例输入2
2 2
样例输出2
21

"""

"""
这个解决方案的工作原理如下：

我们首先计算阶乘数组，用于后续计算。
创建一个包含1到n的数字列表。
将k减1，转换为0基索引。
从最高位到最低位，我们计算每一位应该是哪个数字：

使用 k // factorial[i] 确定当前位置的索引。
更新k为 k % factorial[i]，准备下一位的计算。
将选中的数字添加到结果中，并从可用数字列表中移除。


最后，将结果数组合并为字符串并返回。

这个方法的时间复杂度是O(n)，比之前的DFS方法要高效得多，尤其是对于大的n和k值。
对于给定的例子：

当n=3, k=3时，输出"213"
当n=2, k=2时，输出"21"

这个解决方案能够正确处理所有的输入情况，并且比之前的DFS方法更加高效。
"""
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        factorial = [1]
        for i in range(1, n):
            factorial.append(factorial[-1] * i)
        
        nums = list(range(1, n+1))
        k -= 1  # Convert to 0-based index
        result = []
        
        for i in range(n-1, -1, -1):
            idx = k // factorial[i]
            k %= factorial[i]
            
            result.append(str(nums[idx]))
            nums.pop(idx)
        
        return ''.join(result)

# Test the solution
sol = Solution()
print(sol.getPermutation(3, 3))  # Should output "213"
print(sol.getPermutation(2, 2))  # Should output "21"
