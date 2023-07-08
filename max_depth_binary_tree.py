class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    def __init__(self) -> None:
        self.max_depth = 0
    def maxDepth(self,root):
        self.preorder_recur(root,depth=1)
        return self.max_depth
    
    def preorder_recur(self,node,depth):
        if node.left != None:
            depth+=1
            depth = self.preorder_recur(node.left,depth)
        if node.right != None:
            depth+=1
            depth = self.preorder_recur(node.right,depth)
        if node.left == None and node.right == None:
            if depth > self.max_depth:
                self.max_depth = depth
            depth-=1
            return depth
        return depth - 1

root = Node(1)
root.left = Node(3)
root.right = Node(2)
root.left.left = Node(4)

print(Solution().maxDepth(root))

