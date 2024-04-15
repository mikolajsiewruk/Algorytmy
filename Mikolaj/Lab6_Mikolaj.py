
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self. right = None
        self.balance = 0

class BST:
    def __init__(self, arr: list):
        self.arr = arr
        self.root = TreeNode(self.arr[0])
        self.make_tree()

    def make_tree(self):
        for nums in self.arr[1:]:
            self.insert(self.root,nums)

    def traverse(self,node):
        if node is not None:
            self.traverse(node.left)
            print(node.value)
            self.traverse(node.right)

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
                        return self.search(node.right, value)
                else:
                    if node.left == None:
                        return 1
                    else:
                        return self.search(node.left, value)
    def remove(self,node,value):
        if not node:
            return 1
        else:
            if node.value > value:
                node.left = self.remove(node.left,value)
                return node
            elif node.value < value:
                node.right = self.remove(node.right,value)
                return node
            else:
                if not node.left and not node.right:
                    del node
                elif not node.left:
                    a = node.right.value
                    del node.right
                    node = TreeNode(a)
                    return node

                elif not node.right:
                    a = node.left.value
                    del node.left
                    node = TreeNode(a)
                    return node
                else:
                    parent = node
                    successor = node.right
                    while successor.left is not None:
                        parent = successor
                        successor = successor.left
                        if parent != node:
                            parent.left = successor.right
                        else:
                            parent.right = successor.right
                        del successor
                        return node
    def find_min(self,node):
        if node:
            if node.left is not None:
                return self.find_min(node.left)
            else:
                return node
        else:
            return 1

    def find_max(self,node):
        if node:
            if node.right is not None:
                return self.find_max(node.right)
            else:
                return node
        else:
            return 1
    def find_previous(self, value):
        node = self.search(self.root, value)
        if node.left:
            return self.find_max(node.left)
        else:
            print('lol idk yet')
            #smth





class AVL(BST):

    def check_balance(self,node):
        if node == None:
            return 0
        else:
            return max(self.check_balance(node.left),self.check_balance(node.right)) + 1

    def rotate_right(self,node):
        R = node.left
        node.left = R.right
        R.right = node
        node = R

    def rotate_left(self,node):
        L = node.right
        node.right = L.left
        L.left = node
        node = L

    def balance(self,node):
        balance_factor = self.check_balance(node.left) - self.check_balance(node.right)
        while balance_factor not in [-1,0,1]:
            # print(balance_factor)
            if balance_factor > 1:
                # print('left lacking')
                self.rotate_right(node)
            else:
                # print('right')
                self.rotate_left(node)
            balance_factor = self.check_balance(node.left) - self.check_balance(node.right)
            # print(node.value)
    def insert(self,node,value): # fix to check every node for balance
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
        balance_factor = self.check_balance(node.left) - self.check_balance(node.right)
        if balance_factor not in [-1,0,1]:
            self.balance(node)




'''a=[5,1,8,7,3,10,11,13,14,15,16,17]
b=BST(a)
for el in a[1:]:
    b.insert(b.root,el)
b.insert(b.root,4)
b.remove(b.root,4)
avl = AVL(a)
 elem in a[1:]:
    print(elem)
    avl.insert(avl.root,elem)
print(avl.root.value)
print(avl.check_balance(avl.root.left),avl.check_balance(avl.root.right))
#print(b.root.left.value,b.root.right.value)'''
