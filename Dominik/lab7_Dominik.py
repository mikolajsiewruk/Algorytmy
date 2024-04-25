from tabulate import tabulate
import matplotlib.pyplot as plt
import time as tm

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

    def encode(self, node: HuffmanTreeNode, letter: str, code: str) -> str:
        """
        Returns letter code in Huffman Compression Tree. Initialize with code = "".
        """
        if node:
            if letter == node.letter:
                return code
            if letter in node.left.letter:
                code += "0"
                return self.encode(node.left, letter, code)
            else:
                code += "1"
                return self.encode(node.right, letter, code)
        else:
            return code

    def decode(self,node: HuffmanTreeNode,code: str) -> str:
        """
        Returns a letter represented by the given Huffman letter code.
        """
        if len(code) == 0:
            return node.letter
        if code[0] == '0':
            return self.decode(node.left, code[1:])
        else:
            return self.decode(node.right, code[1:])


    def counting(self, text: str, letter: str):
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
        return print("Nie ma takiej litery")

    def bits(self, node: HuffmanTreeNode, text: str):
        bits_original = len(text) * 8
        bits_Huffman = 0
        unique_characters = []
        for letters in text:
            if letters not in unique_characters:
                unique_characters.append(letters)
        for character in unique_characters:
            code = self.encode(node, character, "")
            bits_Huffman += len(code)

        return bits_original, bits_Huffman

    def as_instruction_wants_wtf(self, node: HuffmanTreeNode, text:str):
        unique_characters = []
        tab = []
        for letters in text:
            if letters not in unique_characters:
                unique_characters.append(letters)
        for character in unique_characters:
            amount = self.counting(text, character)
            code = self.encode(node, character, "")
            tab.append([character, amount, code])

        return print(tabulate(tab))

    def encode_text(self, node, text):
        binary_text = ""
        for letter in text:
            code = self.encode(node, letter, "")
            code = "".join(code)
            binary_text += code
        return binary_text

    def decode_text(self, node, text):
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


c = Compressor()

wers1 = open("1wers.txt", "r")
wers1 = wers1.read()
w1 = c.huffman_compression(wers1)
wers5 = open("5wers.txt", "r")
wers5 = wers5.read()
w5 = c.huffman_compression(wers5)
wers10 = open("10wers.txt", "r")
wers10 = wers10.read()
w10 = c.huffman_compression(wers10)
wers25 = open("test.txt", "r")
wers25 = wers25.read()
w25 = c.huffman_compression(wers25)
# print(len(s))

# print(l)
print("Literka L w kodzie binarnym: " + c.encode(w25, 'L', ""))
print("Kod 0110 jako literka: " + c.decode(w25, '0110'))
print("Ilość wystąpień literki 'a' w tekście: ", c.counting(wers25, "a"))
print('Ilość bitów przed kompresją: ' + str(c.bits(w25, wers25)[0]) + " i po kompresji: " + str(c.bits(w25, wers25)[1]))
c.as_instruction_wants_wtf(w25, wers25)
enc = c.encode_text(w25, wers25)
print("Teskt binarny: " + enc)
print("Tekst zdekodowany: \n" + c.decode_text(w25, enc))


bitso1, bitsd1 = c.bits(w1, wers1)
bitso5, bitsd5 = c.bits(w5, wers5)
bitso10, bitsd10 = c.bits(w10, wers10)
bitso25, bitsd25 = c.bits(w25, wers25)
bitso = [bitso1, bitso5, bitso10, bitso25]
bitsd = [bitsd1, bitsd5, bitsd10, bitsd25]
# print(bitso)
# print(bitsd)
characters = [len(wers1), len(wers5), len(wers10), len(wers25)]

start = tm.perf_counter_ns()
enc1 = c.encode_text(w1, wers1)
stop = tm.perf_counter_ns()
timeenc1 = stop - start
start = tm.perf_counter_ns()
enc5 = c.encode_text(w5, wers5)
stop = tm.perf_counter_ns()
timeenc5 = stop - start
start = tm.perf_counter_ns()
enc10 = c.encode_text(w10, wers10)
stop = tm.perf_counter_ns()
timeenc10 = stop - start
start = tm.perf_counter_ns()
enc25 = c.encode_text(w25, wers25)
stop = tm.perf_counter_ns()
timeenc25 = stop - start
times_enc = [timeenc1, timeenc5, timeenc10, timeenc25]

start = tm.perf_counter_ns()
dec1 = c.decode_text(w1, enc1)
stop = tm.perf_counter_ns()
timedec1 = stop - start
start = tm.perf_counter_ns()
dec5 = c.decode_text(w5, enc5)
stop = tm.perf_counter_ns()
timedec5 = stop - start
start = tm.perf_counter_ns()
dec10 = c.decode_text(w10, enc10)
stop = tm.perf_counter_ns()
timedec10 = stop - start
start = tm.perf_counter_ns()
dec25 = c.decode_text(w25, enc25)
stop = tm.perf_counter_ns()
timedec25 = stop - start
times_dec = [timedec1, timedec5, timedec10, timedec25]

coefficiant1 = bitsd1/bitso1 * 100
coefficiant5 = bitsd5/bitso5 * 100
coefficiant10 = bitsd10/bitso10 * 100
coefficiant25 = bitsd25/bitso25 * 100
coefficiants = [coefficiant1, coefficiant5, coefficiant10, coefficiant25]


plt.figure(1)
plt.plot(characters, bitso, label = "Bits before compression")
plt.plot(characters, bitsd,  label="Bits after compression")
plt.xlabel("Długość tekstu")
plt.ylabel("Ilość bitów")
plt.title("Zależność ilości bitów od ilości znaków")
plt.legend()
plt.grid(True)

plt.figure(2)
plt.plot(characters, times_enc, label = "Time for compression")
plt.plot(characters, times_dec, label = "Time for decompression")
plt.xlabel("Długość tekstu")
plt.ylabel("Czas [ns]")
plt.title("Zależność czasu od ilości znaków")
plt.legend()
plt.grid(True)

plt.figure(3)
plt.plot(characters, coefficiants, label = "Level of compression")
plt.xlabel("Długość tekstu")
plt.ylabel("Poziom kompresji")
plt.title("Zależność długości tekstu od poziomu kompresji")
plt.legend()
plt.grid(True)

plt.show()

