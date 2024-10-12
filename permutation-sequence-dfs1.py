"""
这个DFS解决方案的工作原理如下：

我们定义了一个内部函数dfs，它接受当前的排列cur和一个计数器count作为参数。
dfs函数的工作流程：

如果已经找到了第k个排列，直接返回。
如果当前排列的长度等于n，说明我们生成了一个完整的排列：

增加计数器
如果这是第k个排列，我们保存结果并标记为已找到
返回继续搜索


对于1到n的每个数字：

如果这个数字还没有被使用：

将它添加到当前排列
递归调用dfs
如果找到了结果，返回
否则，回溯（移除最后添加的数字）


为了避免产生重复的排列,可以用一个布尔数组来标记每个数字是否已经被使用过。每次填入一个数字,就将其标记为已使用;
回溯时(回到上一层递归，还未被标记),再将其标记为未使用。



在主函数中，我们初始化结果字符串和标志变量，然后调用dfs函数。
最后返回找到的第k个排列。

这个解决方案的时间复杂度在最坏情况下是O(n!)，因为它可能需要生成所有的排列。对于大的n和k，这个方法会比基于数学的解法慢得多。但是，它直观地展示了如何使用DFS来生成排列，并且在找到第k个排列后立即停止，避免了不必要的计算。
对于给定的例子：

当n=3, k=3时，输出"213"
当n=2, k=2时，输出"21"

这个DFS解决方案能够正确处理所有的输入情况，并且直接对应了题目中描述的排列生成过程。
"""



class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def dfs(cur, count):
            """
            cur: 当前已经产生的排列(字符串形式)
            count: 当前已经产生的排列数
            """
            nonlocal k, res
            # 如果已经产生了 k 个排列,就可以返回了
            if count == k:
                res = cur
                return
            # 依次尝试填入每个未使用的数字
            for i in range(1, n + 1):
                if not used[i]:
                    used[i] = True
                    dfs(cur + str(i), count + 1)
                    # 回溯
                    used[i] = False

        # 初始化结果和标记数组
        res = ''
        used = [False] * (n + 1)
        # 开始 DFS
        dfs('', 0)
        return res

sol = Solution()
print(sol.getPermutation(3, 3))  # Should output "213"
print(sol.getPermutation(2, 2))  # Should output "21"