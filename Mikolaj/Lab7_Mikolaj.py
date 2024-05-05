from tabulate import tabulate

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
            """
            Helper function for sorting items list.
            """
            return item[1]

        unique_characters = []
        dictionary = {}
        for letters in text:  # dodanie wszystkich znaków do listy bez powtórzeń
            if letters not in unique_characters:
                unique_characters.append(letters)
        for letters in unique_characters:  # utworzenie słownika gdzie key = litera, value = ilość wystąpień
            dictionary[letters] = text.count(letters)
        dictionary_desc = dict(sorted(dictionary.items(), key=lambda item: -item[1]))  # posortowanie słownika
        items = []
        i = dictionary_desc.items()
        for item in i:  # dodanie itemów w słowniku do listy (łatwiejsza modyfikacja później) (w zasadzie można pominąć w ogóle tworzenie słownika ale już niech działa tak jak jest)
            items.append([item[0], item[1]])

        items.sort(key=lambda item:item[1], reverse=True)  # sortowanie listy wg ilości wystąpień, można to zrobić niby lambdą, ale idk czemu lambda dawała mi różne wyniki, tzn lista była posortowana dobrze wg wartości, ale litery o tych samych ilościach były różnie ustawiane, przez co drzewo robiło się inaczej i kody były różne, stąd została funkcja pomocnicza, możesz przetestowac lambdę

        while len(items) > 1:  # algorytm kompresji Huffmana
            # mój pomysł na to był taki, jeśli dwa ostatnie itemy w liście to pojedyncze litery, stworzyć dla nich Nody i dodać do listy item np. ['ab', 2(suma liczby wystapien), Powstały node]
            i1 = items[-1]
            i2 = items[-2]
            if len(i1) == 2 and len(i2) == 2:  # przypadek 1: oba itemy nie są reprezentowane przez żaden node
                root = HuffmanTreeNode(i1[1] + i2[1], i1[0] + i2[0])  # stwórz node sumujący
                root.left = HuffmanTreeNode(i1[1], i1[0])  # dodaj rootowi liście
                root.right = HuffmanTreeNode(i2[1], i2[0])
                items.pop(items.index(i1))  # usuń litery z listy
                items.pop(items.index(i2))
                t = i1[0] + i2[0]
                val = i1[1] + i2[1]
                items.append([t, val, root])  # w ich miejsce dodaj item reprezentujący obie litery
                items.sort(key=keys, reverse=True)
            elif len(i1) == 2 and len(i2) != 2:  # przypadek 2: lewy item nie jest nodem, prawy jest
                root = HuffmanTreeNode(i1[1] + i2[1], i1[0] + i2[0])
                root.left = HuffmanTreeNode(i1[1], i1[0])
                root.right = i2[2]
                items.pop(items.index(i1))  # najlepszy designer zastapilby fragment odtąd
                items.pop(items.index(i2))
                t = i1[0] + i2[0]
                val = i1[1] + i2[1]
                items.append([t, val, root])
                items.sort(key=keys, reverse=True)  # dotąd, funkcją robiącą to raz, żeby nie powielać kodu 4 razy, polecam to zrobić dla każdego przypadku
            elif len(i1) != 2 and len(i2) == 2:  # przypadek 3 lewy jest nodem, prawy nie jest
                root = HuffmanTreeNode(i1[1] + i2[1], i1[0] + i2[0])
                root.left = i1[2]
                root.right = HuffmanTreeNode(i2[1], i2[0])
                items.pop(items.index(i1))
                items.pop(items.index(i2))
                t = i1[0] + i2[0]
                val = i1[1] + i2[1]
                items.append([t, val, root])
                items.sort(key=keys, reverse=True)
            else:  # przypadek 4 oba itemy są nodami
                root = HuffmanTreeNode(i1[1] + i2[1], i1[0] + i2[0])
                root.left = i1[2]
                root.right = i2[2]
                items.pop(items.index(i1))
                items.pop(items.index(i2))
                t = i1[0] + i2[0]
                val = i1[1] + i2[1]
                items.append([t, val, root])
                items.sort(key=keys, reverse=True)

        return items[0][2]  # zwraca root tego drzewa

    def encode(self, node: HuffmanTreeNode, letter: str, code: list) -> list:
        """
        Returns letter code in Huffman Compression Tree. Initialize with code = [].
        """
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

    def decode(self,node: HuffmanTreeNode,code: list) -> str:
        """
        Returns a letter represented by the given Huffman letter code.
        """
        if not code:
            return node.letter
        for i in code:
            code.pop(code.index(i))
            if i == 0:
                return self.decode(node.left,code)
            else:
                return self.decode(node.right,code)


    def counting(self, text: str, letter: str):
        """
        Counts a given letter in a given string.
        """
        unique_characters = []
        dictionary = {}
        for letters in text:
            if letters not in unique_characters:
                unique_characters.append(letters)
        for letters in unique_characters:
            dictionary[letters] = text.count(letters)
        for key in dictionary.keys():
            if letter == key:
                return dictionary.get(key)
        return 1

    def bits(self, node: HuffmanTreeNode, text: str):
        """
        Returns the number of bits used by a given text.
        """
        bits_original = len(text) * 8
        bits_Huffman = 0
        unique_characters = []
        for letters in text:
            if letters not in unique_characters:
                unique_characters.append(letters)
        for character in unique_characters:
            code = self.encode(node, character, [])
            bits_Huffman += len(code)

        return bits_original, bits_Huffman

    def as_instruction_wants(self, node: HuffmanTreeNode, text: str):
        """
        Creates a table.
        """
        unique_characters = []
        tab = []
        for letters in text:
            if letters not in unique_characters:
                unique_characters.append(letters)
        for character in unique_characters:
            amount = self.counting(text, character)
            code = self.encode(node, character, [])
            tab.append([character, amount, code])

        print(tabulate(tab))

    def encode_text(self, node: HuffmanTreeNode, text: str):
        binary_text = []
        for letter in text:
            code = self.encode(node, letter, [])
            code.append(code)
            binary_text += code
        return binary_text

    def decode_text(self, node: HuffmanTreeNode, text: list):
        original_text = ""
        end = 0
        while len(text) > 0:
            character = text[0:end]
            encoded = self.decode(node, character)
            if len(encoded) == 1:
                original_text += encoded
                text = text[end:]
                end = 0
            else:
                end = end + 1
        return original_text


s = open("l7.txt", "r")
s = s.read()
c = Compressor()

# text is a root node of a Huffman compression tree
text = c.huffman_compression(s)

print(c.encode(text,'L',[]))
print(c.decode(text,[0,1,1,0]))
print(c.counting(s, "a"))

print('Ilość bitów przed kompresją: ' + str(c.bits(text, s)[0]) + " i po kompresji: " + str(c.bits(text, s)[1]))
enc = c.encode_text(text, s)
print(enc)
c.as_instruction_wants(text, s)
#print(c.decode_text(text, enc))
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