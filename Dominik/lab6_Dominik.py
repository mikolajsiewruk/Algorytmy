class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self, arr: list):
        self.arr = arr
        self.root = Node(self.arr[0])

    def minimum(self, node):
        minimum = node.key
        if node.left:
            minimum = self.minimum(node.left)
        return minimum
    def next(self, node):
        if node.right:
            return self.minimum(node.right)
        else:
            return None



    def insert(self, node, key):
        if node.key:
            if key < node.key:
                if node.left is None:
                    node.left = Node(key)
                else:
                    self.insert(node.left, key)
            else:
                if node.right is None:
                    node.right = Node(key)
                else:
                    self.insert(node.right, key)
        else:
            node.key = key

    def remove(self, node, key):
        if node.key:
            if key < node.key:
                node.left = self.remove(node.left, key)
                return node
            elif key > node.key:
                node.right = self.remove(node.right, key)
                return node
            else:
                if node.left is None and node.right is None:
                    del node
                elif node.left:
                    node.key = node.left.key
                    del node.left
                elif node.right:
                    node.key = node.right.key
                    del node.right
                else:
                    print("No such node")


a=[5,1,8,7,3,10,11,13,14,15,16,17]
b=BST(a)
for el in a[1:]:
    b.insert(b.root,el)
b.insert(b.root,4)
print(b.next(b.root.left))