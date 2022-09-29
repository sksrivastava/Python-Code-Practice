class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def diameter(root):
    if root is None:
        return 0
    global res
    l = diameter(root.left)
    r = diameter(root.right)
    temp = max(l, r) + 1
    ans = (1 + l + r)
    res = max(res, ans)
    return temp



res = float('-inf')
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.left = Node(6)
root.left.right.right = Node(7)
root.left.right.left.left = Node(8)
diameter(root)
print("diameter "+ str(res))