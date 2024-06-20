import random as rnd

def generate_text():
    length = rnd.randint(5,15)
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B',
        'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
        'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0','1','2','3','4','5','6','7','8','9'
    ]
    s = []
    for i in range(length):
        s.append(str(rnd.choice(letters)))


    return s

def generate_hash(string):
    hash = {s:ord(  s) for s in string}
    return hash



def adding_hash(string):
    hash = generate_hash(string)

    s = 0
    for chr in string:
        s+= hash[chr]
    return s


def modulo_hash(string):
    number = 7
    h = adding_hash(string)
    return h % number

def multiplication_hash(string):
    A = 0.3333
    m = 10000
    h = adding_hash(string)
    rest = h*A % 1
    return int(rest*m)

def random_hash(string):
    r = rnd.random()
    h=adding_hash(string)
    return int(r*h)

l = [random_hash,multiplication_hash,adding_hash,modulo_hash]

def custom_hash(hashing_methods, string,depth):
    hashed = string
    for i in range(depth):
        method = rnd.choice(hashing_methods)
        hashed = method(str(hashed))

    return hashed

print(adding_hash('str'))
print(modulo_hash('str'))
print(multiplication_hash('str'))
print(random_hash('str'))

print(custom_hash(l,'str',2))