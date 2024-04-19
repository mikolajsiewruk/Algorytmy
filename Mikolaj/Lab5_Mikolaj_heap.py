import random
import networkx as nx
import matplotlib.pyplot as plt
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
        self.graph=[]
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
                self.graph.append((f'{current.val}',f'{current.left.val}'))
                break
            else:
                q.append(current.left)
            if not current.right:
                print(f"{current.val}  added {val} right")
                current.right = TreeNode(val)
                self.graph.append((f'{current.val}',f'{current.right.val}'))
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
        return self.graph
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
    used=[]
    while len(t)<10:
        a=random.randint(1,50)
        if a not in used:
            t.append(a)
            used.append(a)
    return t


s=Tree([1,2,3,4,5])
s.make_tree()
s.print_tree(s.root)
vec=generate_vector()
h=MaxHeap(vec)
g=h.make_heap()
print(g)
G=nx.Graph()
G.add_edges_from(g)


# grafowanie z neta wzięte
def hierarchy_pos(G, root=None, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5):
    '''
    From Joel's answer at https://stackoverflow.com/a/29597209/2966723.
    Licensed under Creative Commons Attribution-Share Alike

    If the graph is a tree this will return the positions to plot this in a
    hierarchical layout.

    G: the graph (must be a tree)

    root: the root node of current branch
    - if the tree is directed and this is not given,
      the root will be found and used
    - if the tree is directed and this is given, then
      the positions will be just for the descendants of this node.
    - if the tree is undirected and not given,
      then a random choice will be used.

    width: horizontal space allocated for this branch - avoids overlap with other branches

    vert_gap: gap between levels of hierarchy

    vert_loc: vertical location of root

    xcenter: horizontal location of root
    '''
    if not nx.is_tree(G):
        raise TypeError('cannot use hierarchy_pos on a graph that is not a tree')

    if root is None:
        if isinstance(G, nx.DiGraph):
            root = next(iter(nx.topological_sort(G)))  # allows back compatibility with nx version 1.11
        else:
            root = random.choice(list(G.nodes))

    def _hierarchy_pos(G, root, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5, pos=None, parent=None):
        '''
        see hierarchy_pos docstring for most arguments

        pos: a dict saying where all nodes go if they have been assigned
        parent: parent of this branch. - only affects it if non-directed

        '''

        if pos is None:
            pos = {root: (xcenter, vert_loc)}
        else:
            pos[root] = (xcenter, vert_loc)
        children = list(G.neighbors(root))
        if not isinstance(G, nx.DiGraph) and parent is not None:
            children.remove(parent)
        if len(children) != 0:
            dx = width / len(children)
            nextx = xcenter - width / 2 - dx / 2
            for child in children:
                nextx += dx
                pos = _hierarchy_pos(G, child, width=dx, vert_gap=vert_gap,
                                     vert_loc=vert_loc - vert_gap, xcenter=nextx,
                                     pos=pos, parent=root)
        return pos

    return _hierarchy_pos(G, root, width, vert_gap, vert_loc, xcenter)
pos = hierarchy_pos(G,f'{h.root.val}') # tutaj dodać root
nx.draw(G, pos=pos, with_labels=True)
plt.savefig('hierarchy.png')