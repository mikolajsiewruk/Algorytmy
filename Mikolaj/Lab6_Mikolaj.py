
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self. right = None

class BST:
    def __init__(self, arr: list):
        self.arr = arr
        self.root = TreeNode(self.arr[0])
        self.make_tree()  # z tą linijką kodu drzewa utworzą się automatycznie z wartości podanych w tabeli arr, jednak można dodać inne wartości ręcznie poprzez insert (przykład na dole)

    def make_tree(self):
        """
        Inserts array values into a Tree structure.
        """
        for nums in self.arr[1:]:
            self.insert(self.root,nums)

    def traverse(self,node):
        """
        Prints inorder traverse of a Tree.
        """
        if node is not None:
            self.traverse(node.left)
            print(node.value)
            self.traverse(node.right)

    def insert(self,node,value):
        if node.value:
            if value > node.value:  # jeśli jest większe to wstaw z prawej
                if node.right is None:
                    node.right = TreeNode(value)
                else:
                    self.insert(node.right,value)
            else:  # jesli mniejsze to wstaw z lewej
                if node.left is None:  # jeśli nie ma lewego węzła to wstaw
                    node.left = TreeNode(value)
                else:  # jeśli jest to kontynuuj wstawianie
                    self.insert(node.left,value)
        else:
            node.value = value

    def search(self,node,value):
        """
        Returns TreeNode object with a given value.
        """
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
            if node.value > value:  # jeśli wartość mniejsza od wartości węzła to usuwaj z lewej
                node.left = self.remove(node.left,value)
                return node
            elif node.value < value:
                node.right = self.remove(node.right,value)
                return node
            else:  # jeśli wartość węzła = value
                if not node.left and not node.right:  # jeśli nie ma żadnych dzieci można usunąć węzeł i tyle
                    del node
                elif not node.left:  # jeśli nie ma lewego dziecka podstawiamy prawe dziecko węzła za węzeł
                    a = node.right.value
                    del node.right
                    node = TreeNode(a)
                    return node

                elif not node.right:  # jeśli nie ma prawego dziecka podstawiamy lewe dziecko za węzeł
                    a = node.left.value
                    del node.left
                    node = TreeNode(a)
                    return node
                else:  # jeśli istnieją lewe i prawe dziecko robimy to coś
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
            return "TBC"  # to be continued however never will be, weź z neta

    def find_next(self,value):
        node = self.search(self.root, value)
        if node.right:
            return self.find_min(node.right)
        else:
            return "TBC"


class AVL(BST):  # klasa avl dziedziczy metody i argumenty przy inizjalizacji od BST, metody zdefiniowane dla BST działają zawsze dla AVL, jedyną różnicą będzie balansowanie drzewa AVL poprzez rotacje przy dodawaniu i usuwaniu węzłów

    def check_balance(self,node):
        """
        Returns height of left and right subtree of a node.
        """
        if node == None:
            return 0
        else:
            return max(self.check_balance(node.left),self.check_balance(node.right)) + 1

    def rotate_right(self,node):
        R = node.left  # schemat rotacji jak w instrukcji
        node.left = R.right
        R.right = node
        node = R

    def rotate_left(self,node):
        L = node.right
        node.right = L.left
        L.left = node
        node = L

    def balance(self,node):
        # balance factor to wysokość lewego poddrzewa - wysokość prawego
        balance_factor = self.check_balance(node.left) - self.check_balance(node.right)
        while balance_factor not in [-1,0,1]:
            if balance_factor > 1:  # jeśli jest większy niż jeden to znaczy że lewe poddrzewo jest dłuższe, więc należy zrotować węzeł w prawo
                self.rotate_right(node)
            else:
                self.rotate_left(node)
            balance_factor = self.check_balance(node.left) - self.check_balance(node.right)  # ponowne obliczenie balance factor gdyby jedna rotacja nie wystarczyła
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
        # wstawianie takie samo jak BST z różnicą balansowania
        balance_factor = self.check_balance(node.left) - self.check_balance(node.right)
        if balance_factor not in [-1,0,1]:
            self.balance(node)

    def remove(self, node, value):
        if not node:
            return 1
        else:
            if node.value > value:
                node.left = self.remove(node.left, value)
                return node
            elif node.value < value:
                node.right = self.remove(node.right, value)
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
            balance_factor = self.check_balance(self.root.left) - self.check_balance(self.root.right)
            if balance_factor not in [-1, 0, 1]:
                self.balance(self.root)



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
