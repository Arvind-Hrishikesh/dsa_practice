'''
Given a binary tree, find its preorder traversal.
'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None


#Function to return a list containing the preorder traversal of the tree.
def preorder(root):
    res=[]
    nodes_visited=[]
    try:
        root_node = root
    except:
        print("Incorrect input")
    
    current_node = root_node
    if current_node.left == None and current_node.right==None:
        print(current_node.data)
    nodes_visited.append(current_node)
    res.append(current_node.data)
    count=-1
    while 1>0:
        if current_node == root_node and (current_node.left in nodes_visited or current_node.left == None ) and (current_node.right in nodes_visited or current_node.right == None):
            break
        elif current_node.left != None and current_node.left not in nodes_visited:
            current_node = current_node.left
            nodes_visited.append(current_node)
            res.append(current_node.data)
            count=-1
            
        elif current_node.right != None and current_node.right not in nodes_visited:
            current_node = current_node.right
            nodes_visited.append(current_node)
            res.append(current_node.data)
            count=-1
        
        elif (current_node.left in nodes_visited and current_node.right in nodes_visited and current_node in nodes_visited) or (current_node.left == None and current_node.right == None and current_node in nodes_visited):
            current_node = nodes_visited[count]
            count-=1
    
    return res

root = Node(1)
root.left=Node(2)
root.left.left=Node(3)
root.left.right=Node(4)

pre_path = preorder(root)

for _ in pre_path:
    print(str(_)+" ",end='')
print()

        
