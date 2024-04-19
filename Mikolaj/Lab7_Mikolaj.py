

class HuffmanTreeNode:
    def __init__(self,value,letter):
        self.value = value
        self.left = None
        self.right = None
        self.letter = letter

    def add_node(self,node,val,letter):
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
                current.left=HuffmanTreeNode(val,letter) # jesli nie to dodaj lewego nołda i zakończ sprawdzanie
                break
            else:
                q.append(current.left)
            if not current.right: # to samo co dla lewej strony
                print(f"{current.val}  added {val} right")
                current.left = HuffmanTreeNode(val, letter)
                break
            else:
                q.append(current.right)
unique_characters = set()
dictionary = {}
st = ''
file = open("l7.txt",mode = "r")
for lines in file:
    st+=lines
    for chars in lines:
        unique_characters.add(chars)
for letters in unique_characters:
    dictionary[letters] = st.count(letters)
print(unique_characters)
print(dictionary)
dictionary_desc = dict(sorted(dictionary.items(), key=lambda item: -item[1]))

print(dictionary_desc)
items = []
i = dictionary_desc.items()
for item in i:
    items.append([item[0],item[1]])

def keys(item):
    return item[1]
items.sort(key = keys,reverse=True)
print(items)

while len(items)>1:
    i1 = items[-1]
    i2 = items[-2]
    n1 = HuffmanTreeNode(i1[1]+i2[2],i1[0]+i2[0])