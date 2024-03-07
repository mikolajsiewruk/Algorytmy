class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

def nawiasy(Ciag_nawiasow):
    stos = Stack()
    for nawias in Ciag_nawiasow:
        if nawias == '(':
            stos.push('(')
        elif nawias == ')' and stos.isEmpty() == False:
            stos.pop()
        elif nawias != '(' and nawias != ')':
            continue
        else:
            return False
    return stos.isEmpty()

n = '((()))'
print(nawiasy(n))

def parentheses(parentheses_string):
    stos = Stack()
    slownik = {
        '(' : ')',
        '[' : ']',
        '{' : '}'
    }
    for char in parentheses_string:
        if char in slownik.keys():
            stos.push(char)
        elif not stos.isEmpty() and char == slownik[stos.peek()]:
            stos.pop()
        elif char not in slownik.keys() and char not in slownik.values():
            continue
        else:
            return False
    return stos.isEmpty()

print(parentheses(''))