
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

def preorder_recur(node,nodes_visited):
    nodes_visited.append(node)
    if node.left != None:
        nodes_visited = preorder_recur(node.left,nodes_visited)
    if node.right != None:
        nodes_visited = preorder_recur(node.right,nodes_visited)
    if node.left == None and node.right == None:
        return nodes_visited
    return nodes_visited
    
def preorder_helper(root):
    nodes_visited = preorder_recur(root,[])
    res=[]
    for node in nodes_visited:
        res.append(node.data)
    
    return res

# Example input
root = Node(1)
root.left = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)

nodes_list = preorder_helper(root)

for node in nodes_list:
    print(node)