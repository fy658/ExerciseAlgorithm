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





