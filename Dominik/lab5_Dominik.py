class Tree:
    def __init__(self, arr):
        self.arr = arr
        self.root = Node(arr[0])

    def make_tree(self):
        for i in range(1, len(self.arr)):
            self.root.insert(self.arr[i])

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = Node(value)
                else:
                    self.left.insert(value)
            elif value > self.value:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.insert(value)
        else:
            self.value = value

    def get_value(self):
        print(self.value)

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.value),
        if self.right:
            self.right.print_tree()


x = Tree([1,2,3,4,5,6,7,8,9])
x.make_tree()
