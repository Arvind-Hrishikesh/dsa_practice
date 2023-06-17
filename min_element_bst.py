class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

def minValue(root):
    node = root
    if node == None:
        return -1
    while 1>0:
        if node.left != None:
            node = node.left
            continue
        else:
            return node.data



root = Node(5)
root.left = Node(3)
root.right = Node(6)
root.left.left = Node(1)
root.right.right = Node(7)

print(minValue(root))

