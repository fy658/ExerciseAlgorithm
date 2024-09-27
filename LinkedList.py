class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


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






