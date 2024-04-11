
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

    def search(self,node,value):
        if not node:
            return False
        else:
            if node.value == value:
                return node
            else:
                if value > node.value:
                    if node.right == None:
                        return 1
                    else:
                        return self.search(node.left, value)
                else:
                    if node.left == None:
                        return 1
                    else:
                        return self.search(node.left, value)

a=[5,1,8,3,10]
b=BST(a)
for el in a[1:]:
    b.insert(b.root,el)
b.insert(b.root,4)
c=b.search(b.root,1)
print(c)
#print(b.root.left.value,b.root.right.value)
