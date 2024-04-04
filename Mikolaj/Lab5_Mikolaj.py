

class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def print_tree(self):
        print(self.data)

    def insert_right(self,num):
        self.right=num
    def insert_left(self,num):
        self.left=num