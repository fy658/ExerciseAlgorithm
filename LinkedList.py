class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


# 反转链表
class Solution1:
    def ReverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        prev = None
        curr = head

        while curr:
            temp_variable = curr.next
            curr.next = prev
            prev = curr
            curr = temp_variable
        return prev


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node1.next = node2
node2.next = node3
cur_node = node1
print("翻转之前：")
while cur_node:
    print(cur_node.val, end=" ")
    cur_node = cur_node.next
solution1 = Solution1().ReverseList(node1)
cur_node = node3
print("\n")
print("翻转之后：")
while cur_node:
    print(cur_node.val, end=" ")
    cur_node = cur_node.next


## 链表在指定区间内翻转

class Solution2:
    def ReverseBetweenInterval(self, head: ListNode, m: int, n: int):
        if not head:
            return None
        dummy_head = ListNode(-1)
        dummy_head.next = head
        prev = dummy_head
        curr = head

        for _ in range(1, m):
            prev = curr
            curr = curr.next

        for _ in range(m, n):
            temp_var = curr.next
            curr.next = temp_var.next
            temp_var.next = prev.next
            prev.next = temp_var
        return dummy_head.next



node_list1 = ListNode(1)
node_list2 = ListNode(2)
node_list3 = ListNode(3)
node_list4 = ListNode(4)
node_list5 = ListNode(5)
node_list1.next = node_list2
node_list2.next = node_list3
node_list3.next = node_list4
node_list4.next = node_list5

current_node = node_list1
print("\nbefore reverse ********")
while current_node:
    print(current_node.val, end=" ")
    current_node = current_node.next

solution2 = Solution2().ReverseBetweenInterval(node_list1,2, 4)
curr_node = node_list1
print("\n")
print("after reverse *********：")
while curr_node:
    print(curr_node.val, end=" ")
    curr_node = curr_node.next


"""
### 给定一个链表，要求将其翻转成如下形式： 
    原链表：L0 -> L1 -> ... -> Ln-1 -> Ln 
    翻转后：L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 -> ... 
    输入输出格式
    输入：一串数字，用逗号分隔，例如 "1,2,3,4,5" 输出：翻转后的数字串，用逗号分隔，例如 "1,5,2,4,3"

"""

# 这是函数的开始。首先检查链表是否为空（not head）或只有一个节点（not head.next）。如果是，直接返回头节点，因为不需要重排。

number_list = "1,2,3,4,5"
class Solution3:
    def create_linked_list(self):
        dummmy = ListNode(0)
        curr = dummmy
        for val in number_list:
            curr.next = ListNode(int(val))
            curr = curr.next
        return dummmy.next

    def reorder_linked_list(self, head):
        head = self.create_linked_list()
        if not head:
            return head
        # 找到链表中点
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        # 分割链表
        second_half = slow.next
        slow.next = None

        # 反转后半部分
        pre, curr = None, second_half
        while curr:
            temp = curr.next
            curr.next = pre
            pre = curr
            curr = temp

        second_half = pre

        # 合并两个链表

        curr_1 = head
        curr_2 = second_half
        while curr_2:
            temp_1 = curr_1.next
            temp_2 = curr_2.next
            curr_1.next = curr_2
            curr_2.next = temp_1
            temp_1 = temp_1.next
            temp_2 = temp_2.next

        return head


"""
描述
给定链表的头节点，旋转链表，将链表每个节点往右移动 k 个位置，原链表后 k 个位置的节点则依次移动到链表头。

即，例如链表 ： 1->2->3->4->5 k=2 则返回链表 4->5->1->2->3
  
示例1
输入：
{1,2,3,4,5},2
返回值：
{4,5,1,2,3}

示例2
输入：
{1,2,3},3
返回值：
{1,2,3}
"""


# 方法1


class Solution4:
    def rotateLinkedList(self, head: ListNode, k: int) -> ListNode:
        # write code here
        if not head:
            return None
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        if k == length:
            return head
        if k > length:
            k = k % length
        # 此处又开始重新重头遍历链表，较复杂，看下面方法如何避免重复遍历链表
        curr = head
        index = 1
        while index < length - k:
            curr = curr.next
            index += 1
        temp = curr.next
        # 从倒数第k+1个位置断开链表
        curr.next = None
        new_head = temp
        dummy = ListNode(0)
        dummy.next = new_head
        new_pre = new_head
        # 再次重新遍历后半部分链表，很麻烦， 看下面方法如何避免重复遍历链表
        while new_pre.next:
            new_pre = new_pre.next
        new_pre.next = head

        return dummy.next

    def rotateLinkedList1(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        curr = head
        length = 1
        while curr.next:
            length += 1
            curr = curr.next
        if k > length:
            k = k % length
        # 将链表尾部指向链表头部，形成循环链表
        curr.next = head
        index = 0
        while index < length - k:
            curr = curr.next
            index += 1
        temp = curr.next
        # 从倒数第k+1个位置断开链表
        curr.next = None
        new_head = temp

        return new_head





