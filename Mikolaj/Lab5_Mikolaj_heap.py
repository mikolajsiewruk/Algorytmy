import random
class TreeNode:
    """
    Individual node of a Tree class.
    """
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class Tree:
    """
    Binary Tree data structure.
    """
    def __init__(self,arr):
        self.arr=arr
        self.root=TreeNode(arr[0])

    def add_node(self,node,val):
        """
        Add a node to the Tree class.
        :param node: Root node
        :param val: Value of a node to add
        :return:
        """
        q=[] # kolejka nołdów do sprawdzenia
        q.append(node)
        # metoda dodaje nołdy od lewej, jeśli chcemy od prawej to trzeba zamienić ify kolejnością
        while q:
            current=q[0] # sprawdzany node to 1. z kolejki
            q.pop(0)
            if not current.left: # sprawdza czy node ma lewą stronę
                print(f"{current.val}  added {val} left")
                current.left=TreeNode(val) # jesli nie to dodaj lewego nołda i zakończ sprawdzanie
                break
            else:
                q.append(current.left)
            if not current.right: # to samo co dla lewej strony
                print(f"{current.val}  added {val} right")
                current.right=TreeNode(val)
                break
            else:
                q.append(current.right)
    def make_tree(self):
        """
        Creates a complete Tree from the initialization array.
        :return:
        """
        for i in range(1,len(self.arr)):
            self.add_node(self.root,self.arr[i])

    def print_tree(self,node):
        """
        Prints values of nodes in a Tree in random order.
        :param node: Root of a Tree
        :return:
        """
        if not node:
            return
        self.print_tree(node.left)
        print(node.val, end=" ")
        self.print_tree(node.right)

class MaxHeap:
    """
    Max Heap data structure.
    """
    def __init__(self,arr):
        self.arr=arr
        self.root=TreeNode(max(self.arr))
        self.arr.remove(max(self.arr))
        self.temp=self.arr

    def add_node(self, node, val):
        """
        Add a node to the Heap class.
        :param node: Root node
        :param val: Value of a node to add
        :return:
        """
        q = []
        q.append(node)
        while q:
            current = q[0]
            q.pop(0)
            if not current.left:
                print(f"{current.val}  added {val} left")
                current.left = TreeNode(val)
                break
            else:
                q.append(current.left)
            if not current.right:
                print(f"{current.val}  added {val} right")
                current.right = TreeNode(val)
                break
            else:
                q.append(current.right)

    def make_heap(self):
        """
        Creates a complete Heap from the initialization array by choosing max value in every step.
        :return:
        """
        temp=self.temp
        for i in range(len(self.temp)):
            m=max(temp)
            self.add_node(self.root,m)
            temp.remove(m)
def heapsort(arr:list)->list: # heapsort bazujący na tworzeniu klasy, mega nieoptymalny nie używam go w porównaniu
    """
    Heap sort the array. Time complexity O(n*log(n))
    :param arr:
    :return: sorted array
    """
    a=arr.copy()
    res=[0 for i in range(len(arr))] # tablica zer do zastąpienia w kolejnych krokach wartościami
    j=0
    while j<len(arr):
        t=a.copy() # kopia wektora konieczna żeby inicjalizacja heapa nie deformowała wejściowej tablicy liczb
        h=MaxHeap(a)
        h.make_heap() #  stwórz kopiec z podanej tablicy
        a=t
        a.remove(h.root.val) # z tablicy usuń największą wartość
        j+=1
        res[-j]=h.root.val  # dodaj do tablicy wynikowej największą wartość w kopcu (zawsze jest to root kopca, gdyż używamy max heap) ( w sumie można wziąć też min heap, wtedy zmienić wszystkie max w kopcu na min i dodawać liczby do res nie od końca lecz od początku, zróbcie sobie to jako test) -1 monster jeśli zrobicie i zastosujecie dobrze min heap (bez czatu, widać różnicę!!)

    return res

def generate_vector():
    t=[]
    for i in range(0,10):
        t.append(random.randint(1,10))
    return t

'''
s=Tree([1,2,3,4,5])
s.make_tree()
s.print_tree(s.root)

h=MaxHeap([1,2,3,4,5])
h.make_heap()'''
vec=generate_vector()
print(vec)
print(heapsort(vec))