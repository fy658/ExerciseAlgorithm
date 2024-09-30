class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(values):
    dummy = ListNode(0)
    current = dummy
    for val in values:
        current.next = ListNode(int(val))
        current = current.next
    return dummy.next

def print_linked_list(head):
    values = []
    current = head
    while current:
        values.append(str(current.val))
        current = current.next
    return ','.join(values)

# 非递归方法
def reorder_list_iterative(head):
    if not head or not head.next:
        return head
    
    # 找到中点
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # 分割链表
    second_half = slow.next
    slow.next = None
    
    # 反转后半部分
    prev, curr = None, second_half
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp
    second_half = prev
    
    # 合并两个链表
    first, second = head, second_half
    while second:
        next_first, next_second = first.next, second.next
        first.next = second
        second.next = next_first
        first, second = next_first, next_second
    
    return head

# 递归方法
def reorder_list_recursive(head):
    if not head or not head.next or not head.next.next:
        return head
    
    # 找到倒数第二个节点
    second_last = head
    while second_last.next.next:
        second_last = second_last.next
    
    # 将最后一个节点移到第二个位置
    last = second_last.next
    second_last.next = None
    last.next = head.next
    head.next = last
    
    # 递归处理剩余部分
    reorder_list_recursive(last.next)
    
    return head

# 测试函数
def test_reorder(input_str, method):
    values = input_str.split(',')
    head = create_linked_list(values)
    
    if method == 'iterative':
        reordered = reorder_list_iterative(head)
    else:
        reordered = reorder_list_recursive(head)
    
    return print_linked_list(reordered)

# 测试样例
input_str = "1,2,3,4,5"
print("输入:", input_str)
print("非递归方法输出:", test_reorder(input_str, 'iterative'))
print("递归方法输出:", test_reorder(input_str, 'recursive'))
