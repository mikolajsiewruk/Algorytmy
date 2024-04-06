class TreeNode:
    """
    Tree Node with custom inserting methods.
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self. right = None

    def insert_left_leaf(self, value):
        self.left = value

    def insert_right_leaf(self, value): # dodanie liścia
        self.right = value

    def insert_left_node(self, value):
        self.left = TreeNode(value)

    def insert_right_node(self, value): # dodanie węzła
        self.right = TreeNode(value)

    def get_value_left(self):
        if type (self.left) == int:
            return self.left
        else:
            return self.left.value

    def get_value_right(self):
        if type (self.right) == int:
            return self.right
        else:
            return self.right.value

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.value)
        if self.right:
            self.right.print_tree()





# nieudana klasa tree, może mieć zastosowanie do czegoś innego (insert sortuje liczby na wejściu)
'''class Tree:
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
        print("xd"),
        if self.right:
            self.right.print_tree()'''


'''x = Tree([1,2,3,4,5,6,7,8,9])
x.make_tree()'''

abc = TreeNode(7)
abc.insert_left_node(8)
abc.insert_right_node(11)
abc.left.insert_left_node(24)
abc.left.insert_right_node(11)
abc.right.insert_left_node(145)
abc.right.insert_right_node(67)
abc.print_tree()