from Lab7_Mikolaj import Compressor

s = 'Ala ma kota'

c = Compressor()

l = c.huffman_compression(s)
print(l)
a = c.encode(l,'m',[])
print(a)
print(c.decode(l,a))