import random as rnd
import numpy as np
import math

l = ["a", "ą", "b", "c", "ć", "d", "e", "ę", "f", "g", "h", "i", "j", "k", "l", "ł", "m", "n", "ń", "o", "ó",
           "p", "q", "r", "s", "ś", "t", "u", "v", "w", "x", "y", "z", "ź", "ż"]
letters = l.copy()
for letter in l:
    letters.append(letter.upper())

def generate_random_text(letters):
    print("Generate random text: select 0")
    print("Type your own text: select 1")
    choice = input()
    if choice == "0":
        text = []
        text_length = rnd.randint(5, 15)
        while len(text) < text_length:
            text.append(letters[rnd.randint(0, len(letters)-1)])
        return text
    elif choice == "1":
        print("Type your own text: ")
        text = str(input())
        for letter in text:
            if letter in letters:
                continue
            else:
                print("Invalid input")
                return 1
        return text
    else:
        print("Invalid input")
        return 2

def hash_dodawanie(text):
    suma = 0
    for letter in text:
        suma += int(ord(letter))
    return suma

def hash_modulo(text):
    suma = hash_dodawanie(text)
    suma = suma%5
    return suma

def hash_mnozenie(text):
    suma = hash_dodawanie(text)
    suma = math.floor(1000*((suma*np.sqrt(2))%1))
    return suma

def hash_random(text):
    suma = hash_dodawanie(text)
    p = rnd.uniform(0, 1)
    suma = int(suma*p)
    return suma

def my_hash(text):
    suma = hash_dodawanie(text)
    r = rnd.randint(100, 1000)
    suma = suma*r
    length = len(str(suma))-2
    suma = int(suma/(10**length))
    return suma

napis = generate_random_text(letters)
print(napis)
print(hash_dodawanie(napis))
print(hash_modulo(napis))
print(hash_mnozenie(napis))
print(hash_random(napis))
print(my_hash(napis))