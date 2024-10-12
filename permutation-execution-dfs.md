# Detailed Execution Process of getPermutation for n=3, k=3

1. Initialize:
   - res = ''
   - used = [False, False, False, False] (index 0 not used)
   - Call dfs('', 0)

2. dfs('', 0):
   - i = 1: used[1] = True, call dfs('1', 1)
   
3. dfs('1', 1):
   - i = 1: skip (already used)
   - i = 2: used[2] = True, call dfs('12', 2)
   
4. dfs('12', 2):
   - i = 1, 2: skip (already used)
   - i = 3: used[3] = True, call dfs('123', 3)
   
5. dfs('123', 3):
   - count == k, so res = '123'
   - Return to previous level

6. Back to dfs('12', 2):
   - used[3] = False (backtrack)
   - No more numbers to try, return to previous level

7. Back to dfs('1', 1):
   - used[2] = False (backtrack)
   - i = 3: used[3] = True, call dfs('13', 2)

8. dfs('13', 2):
   - i = 1: skip (already used)
   - i = 2: used[2] = True, call dfs('132', 3)

9. dfs('132', 3):
   - count == k, so res = '132'
   - Return to previous level

10. Back to dfs('13', 2):
    - used[2] = False (backtrack)
    - No more numbers to try, return to previous level

11. Back to dfs('1', 1):
    - used[3] = False (backtrack)
    - No more numbers to try, return to previous level

12. Back to dfs('', 0):
    - used[1] = False (backtrack)
    - i = 2: used[2] = True, call dfs('2', 1)

13. dfs('2', 1):
    - i = 1: used[1] = True, call dfs('21', 2)

14. dfs('21', 2):
    - i = 1, 2: skip (already used)
    - i = 3: used[3] = True, call dfs('213', 3)

15. dfs('213', 3):
    - count == k, so res = '213'
    - Return to main function

16. Main function:
    - Return res, which is '213'
