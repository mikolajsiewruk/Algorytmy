

class HuffmanTreeNode:
    def __init__(self,value,letter):
        self.value = value
        self.left = None
        self.right = None
        self.letter = letter


class Compressor:

    def huffman_compression(self, text: str) -> HuffmanTreeNode:
        """
        Huffman compression method for any given text.
        Return: Root of a Huffman Compression Tree.
        """
        def keys(item):
            return item[1]

        unique_characters = []
        dictionary = {}
        for letters in text:
            if letters not in unique_characters:
                unique_characters.append(letters)
        for letters in unique_characters:
            dictionary[letters] = text.count(letters)
        dictionary_desc = dict(sorted(dictionary.items(), key=lambda item: -item[1]))
        items = []
        i = dictionary_desc.items()
        for item in i:
            items.append([item[0], item[1]])

        items.sort(key=lambda item:item[1], reverse=True)

        while len(items) > 1:
            i1 = items[-1]
            i2 = items[-2]
            if len(i1) == 2 and len(i2) == 2:
                root = HuffmanTreeNode(i1[1] + i2[1], i1[0] + i2[0])
                root.left = HuffmanTreeNode(i1[1], i1[0])
                root.right = HuffmanTreeNode(i2[1], i2[0])
                items.pop(items.index(i1))
                items.pop(items.index(i2))
                t = i1[0] + i2[0]
                val = i1[1] + i2[1]
                items.append([t, val, root])
                items.sort(key=keys, reverse=True)
            elif len(i1) == 2 and len(i2) != 2:
                root = HuffmanTreeNode(i1[1] + i2[1], i1[0] + i2[0])
                root.left = HuffmanTreeNode(i1[1], i1[0])
                root.right = i2[2]
                items.pop(items.index(i1))
                items.pop(items.index(i2))
                t = i1[0] + i2[0]
                val = i1[1] + i2[1]
                items.append([t, val, root])
                items.sort(key=keys, reverse=True)
            elif len(i1) != 2 and len(i2) == 2:
                root = HuffmanTreeNode(i1[1] + i2[1], i1[0] + i2[0])
                root.left = i1[2]
                root.right = HuffmanTreeNode(i2[1], i2[0])
                items.pop(items.index(i1))
                items.pop(items.index(i2))
                t = i1[0] + i2[0]
                val = i1[1] + i2[1]
                items.append([t, val, root])
                items.sort(key=keys, reverse=True)
            else:
                root = HuffmanTreeNode(i1[1] + i2[1], i1[0] + i2[0])
                root.left = i1[2]
                root.right = i2[2]
                items.pop(items.index(i1))
                items.pop(items.index(i2))
                t = i1[0] + i2[0]
                val = i1[1] + i2[1]
                items.append([t, val, root])
                items.sort(key=keys, reverse=True)

        return items[0][2]

    def encode(self, node, letter, code):
        if node:
            if letter == node.letter:
                return code
            if letter in node.left.letter:
                code.append(0)
                return self.encode(node.left, letter, code)
            else:
                code.append(1)
                return self.encode(node.right, letter, code)
        else:
            return code

    def decode(self,node,code: list):
        if not code:
            return node.letter
        for i in code:
            code.pop(code.index(i))
            if i == 0:
                return self.decode(node.left,code)
            else:
                return self.decode(node.right,code)

'''st = 'Ala ma kota.'
file = open("l7.txt",mode = "r")'''
'''for lines in file:
    st+=lines
    for chars in lines:
        unique_characters.add(chars)'''
'''unique_characters = []
dictionary = {}
for lett in st:
    if lett not in unique_characters:
        unique_characters.append(lett)
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
items.sort(key = keys, reverse=True)
print(items)

while len(items)>1:
    print(items)
    i1 = items[-1]
    i2 = items[-2]
    if len(i1) == 2 and len(i2) == 2:
        root = HuffmanTreeNode(i1[1]+i2[1],i1[0]+i2[0])
        root.left = HuffmanTreeNode(i1[1],i1[0])
        root.right = HuffmanTreeNode(i2[1],i2[0])
        items.pop(items.index(i1))
        items.pop(items.index(i2))
        t = i1[0]+i2[0]
        val = i1[1]+i2[1]
        items.append([t,val,root])
        items.sort(key=keys, reverse=True)
    elif len(i1) == 2 and len(i2) != 2:
        root = HuffmanTreeNode(i1[1]+i2[1],i1[0]+i2[0])
        root.left = HuffmanTreeNode(i1[1],i1[0])
        root.right = i2[2]
        items.pop(items.index(i1))
        items.pop(items.index(i2))
        t = i1[0] + i2[0]
        val = i1[1] + i2[1]
        items.append([t, val, root])
        items.sort(key=keys, reverse=True)
    elif len(i1) != 2 and len(i2) == 2:
        root = HuffmanTreeNode(i1[1] + i2[1], i1[0] + i2[0])
        root.left = i1[2]
        root.right = HuffmanTreeNode(i2[1], i2[0])
        items.pop(items.index(i1))
        items.pop(items.index(i2))
        t = i1[0] + i2[0]
        val = i1[1] + i2[1]
        items.append([t, val, root])
        items.sort(key=keys, reverse=True)
    else:
        root = HuffmanTreeNode(i1[1] + i2[1], i1[0] + i2[0])
        root.left = i1[2]
        root.right = i2[2]
        items.pop(items.index(i1))
        items.pop(items.index(i2))
        t = i1[0] + i2[0]
        val = i1[1] + i2[1]
        items.append([t, val, root])
        items.sort(key=keys, reverse=True)

a = items[0][2]
print(a.decode(a,'m',[]))
print(a.left.right.right.left.letter)'''