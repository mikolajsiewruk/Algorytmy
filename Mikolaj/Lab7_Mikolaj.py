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