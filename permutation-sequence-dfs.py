class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def dfs(cur, count):
            nonlocal result, found
            if found:
                return
            if len(cur) == n:
                count[0] += 1
                if count[0] == k:
                    result = ''.join(map(str, cur))
                    found = True
                return
            
            for i in range(1, n + 1):
                if i not in cur:
                    cur.append(i)
                    dfs(cur, count)
                    if found:
                        return
                    cur.pop()

        result = ""
        found = False
        dfs([], [0])
        return result

# Test the solution
sol = Solution()
print(sol.getPermutation(3, 3))  # Should output "213"
print(sol.getPermutation(2, 2))  # Should output "21"
