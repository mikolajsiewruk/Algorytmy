class Stack:  #deklaracja klasy Stack
    def __init__(self):
        self.items=[]

    def push(self, item):  #dodawanie nowego elementu na wierzchołek stosu
        self.items.append(item)

    def pop(self):       #zwracanie i usuwanie elementu ze stosu
        return self.items.pop ()

    def peek(self):      #odczytywanie elementu bez usuwania
        return self.items[len(self.items)-1]

    def isEmpty(self):   #sprawdzanie czy stos jest pusty
        return self.items == []

    def size(self):      #sprawdzanie rozmiaru stosu
        return len(self.items)

def sprNawiasy(symbolString):
    s=Stack()  #nowy pusty stos
    balanced = True  #nawiasy zrównoważone
    index = 0
    while index < len(symbolString) and balanced: #pętla wykonywana kiedy balanced=True i długość stringu jest większa od 0
        symbol = symbolString[index] #przypisuje do zmiennej symbol index
        if symbol == '(':   #jeżeli "(" to dodajemy do stosu
            s.push(symbol)
        else:
            if s.isEmpty():  #jeżeli ")" i stos jest pusty, nawiasy są niepoprawne
                balanced = False
            else:  #jeżeli ")" i balanced=True to usuwamy nawias otwierający ze stosu
                s.pop()
        index+=1 #przesuwanie się pętli o jeden

    if balanced and s.isEmpty():
        return True     #nawiasy są poprawne
    else:
        return False   #nawiasy są nieporpawne

przyklady = [     #przykłady
        "(()()())",
        "(((())))",
        "(()(((())()))",
        "(())(()))"
    ]
for przyklad in przyklady:
     if sprNawiasy(przyklad):
            print(f"{przyklad}: Poprawne nawiasy") #użycie funkcji f-string który zawiera wartość zmiennej przyklad
     else:
            print(f"{przyklad}: Niepoprawne nawiasy")

def sprNawiasy2(symbolString):
    s2 = Stack()
    balanced = True
    index = 0
    diction = {"(": ")", "[": "]", "{": "}"}  #słownik z odpowiednimi parami nawiasów
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        for symbol in symbolString:
            if symbol in diction.keys(): #jeśli symbol jest w słowniku diction.keys znaczy że jst otwierający i dodajemu go na wierzchołek stosu
                s2.push(symbol)
            elif not s2.isEmpty() and symbol == diction[s2.peek()]: #jeśli symbol jest w słowniku diction to jest zamkykający.Sprawdzamy czy stos nie jest pusty oraz czy nawias zamykający odpowiada typowi nawiasu otwierającego z wierzchu stosu
                s2.pop()                                           #jeżeli warunek spełniony to usuwamy nawias otwierający ze wierzchołka stosu
            else:
                return False                           #w innym wypadku nawiasy niepoprawne
        return s2.isEmpty()

przyklady2 = [
        "([]{}())",
        "{([])[({()})]}",
        "(({}[{()}])]]",
        "({}({([])()})]"
]

for przyklad in przyklady2:
    if sprNawiasy2(przyklad):
        print(f"{przyklad}: Poprawne nawiasy")
    else:
        print(f"{przyklad}: Niepoprawne nawiasy")
