from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_tree(inorder, postorder):
    if not inorder or not postorder:
        return None
    root_value = postorder.pop()
    root = TreeNode(root_value)
    inorder_index = inorder.index(root_value)
    print(inorder.index(root_value))
    root.right = build_tree(inorder[inorder_index + 1:], postorder)
    root.left = build_tree(inorder[:inorder_index], postorder)
    print(root.left)
    return root

def level_order_traversal(root):
    if not root:
        return ""
    queue = deque([root])
    result = []
    while queue:
        node = queue.popleft()
        result.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return "".join(result)

if __name__ == "__main__":
    postorder, inorder = input().split()
    postorder = list(postorder)
    inorder = list(inorder)
    tree = build_tree(inorder, postorder)
    print(level_order_traversal(tree))