# 递归函数执行过程详解

输入: s = "abc", length = 2

初始调用: `count_valid_strings("abc", 2)`
- 初始化 `used = [False, False, False]`
- 初始化 `distinct_str = set()`
- 调用 `generate_diff_string("abc", 2, "", distinct_str, used)`

## 递归过程

1. 第一层递归 (空字符串)
   - 当前: curr = ""
   - 循环 i = 0 ('a')
     - used = [True, False, False]
     - 递归调用: generate_diff_string("abc", 2, "a", distinct_str, used)

2. 第二层递归 (curr = "a")
   - 循环 i = 1 ('b')
     - used = [True, True, False]
     - 递归调用: generate_diff_string("abc", 2, "ab", distinct_str, used)

3. 第三层递归 (curr = "ab")
   - 长度达到2,添加"ab"到distinct_str
   - 返回上一层

4. 回到第二层 (curr = "a")
   - 撤销b的使用: used = [True, False, False]
   - 循环 i = 2 ('c')
     - used = [True, False, True]
     - 递归调用: generate_diff_string("abc", 2, "ac", distinct_str, used)

5. 第三层递归 (curr = "ac")
   - 长度达到2,添加"ac"到distinct_str
   - 返回上一层

6. 回到第一层 (空字符串)
   - 撤销a的使用: used = [False, False, False]
   - 循环 i = 1 ('b')
     - used = [False, True, False]
     - 递归调用: generate_diff_string("abc", 2, "b", distinct_str, used)

7. 第二层递归 (curr = "b")
   - 循环 i = 0 ('a')
     - used = [True, True, False]
     - 递归调用: generate_diff_string("abc", 2, "ba", distinct_str, used)

8. 第三层递归 (curr = "ba")
   - 长度达到2,添加"ba"到distinct_str
   - 返回上一层

9. 回到第二层 (curr = "b")
   - 撤销a的使用: used = [False, True, False]
   - 循环 i = 2 ('c')
     - used = [False, True, True]
     - 递归调用: generate_diff_string("abc", 2, "bc", distinct_str, used)

10. 第三层递归 (curr = "bc")
    - 长度达到2,添加"bc"到distinct_str
    - 返回上一层

11. 回到第一层 (空字符串)
    - 撤销b的使用: used = [False, False, False]
    - 循环 i = 2 ('c')
      - used = [False, False, True]
      - 递归调用: generate_diff_string("abc", 2, "c", distinct_str, used)

12. 第二层递归 (curr = "c")
    - 循环 i = 0 ('a')
      - used = [True, False, True]
      - 递归调用: generate_diff_string("abc", 2, "ca", distinct_str, used)

13. 第三层递归 (curr = "ca")
    - 长度达到2,添加"ca"到distinct_str
    - 返回上一层

14. 回到第二层 (curr = "c")
    - 撤销a的使用: used = [False, False, True]
    - 循环 i = 1 ('b')
      - used = [False, True, True]
      - 递归调用: generate_diff_string("abc", 2, "cb", distinct_str, used)

15. 第三层递归 (curr = "cb")
    - 长度达到2,添加"cb"到distinct_str
    - 返回上一层

16. 递归全部完成
    - distinct_str 包含: {"ab", "ac", "ba", "bc", "ca", "cb"}
    - 返回 len(distinct_str) = 6

