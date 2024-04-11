
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self. right = None

class BST:
    def __init__(self, arr: list):
        self.arr = arr
        self.root = TreeNode(self.arr[0])

    def insert(self,node,value):
        print(node.value)
        if node.value:
            if value > node.value:
                if node.right is None:
                    node.right = TreeNode(value)
                else:
                    self.insert(node.right,value)
            else:
                if node.left is None:
                    node.left = TreeNode(value)
                else:
                    self.insert(node.left,value)
        else:
            node.value = value


a=[5,1,8,3,10]
b=BST(a)
for el in a[1:]:
    b.insert(b.root,el)

print(b.root.left.value,b.root.right.value)
