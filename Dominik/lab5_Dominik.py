class Node1:
    def __init__(self, value):
        self.value = value
        self.left = None
        self. right = None

    def insert_left_leaf(self, value):
        self.left = value

    def insert_right_leaf(self, value):
        self.right = value

    def insert_left_node(self, value):
        self.left = Node1(value)

    def insert_right_node(self, value):
        self.right = Node1(value)

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
        """
        Broken method use at your own risk.
        :return: Something fucked up.
        """
        i=0
        if self.left:
            self.left.print_tree()
            i+=10
        if i!=0 and self.left.left and self.left.right and self.right.left and self.right.right:
            i+=10
        print(i*" " + f"{self.value}") # dodałem jakieś gowno tylko idk jak root odseparować bardziej
        if self.right:
            self.right.print_tree()






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
        print("xd"),
        if self.right:
            self.right.print_tree()


x = Tree([1,2,3,4,5,6,7,8,9])
x.make_tree()

abc = Node1(7)
abc.insert_left_node(8)
abc.insert_right_node(11)
abc.left.insert_left_node(24)
abc.left.insert_right_node(11)
abc.right.insert_left_node(145)
abc.right.insert_right_node(67)
abc.print_tree()