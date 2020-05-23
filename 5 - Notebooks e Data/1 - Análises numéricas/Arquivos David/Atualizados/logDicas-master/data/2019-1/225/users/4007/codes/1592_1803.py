from numpy import*
codigo = input("codigo: ")
a = g[0:] * 5
b = g[:1] * 4
c = g[2] * 3
d = g[3] * 2
e = (a + b + c + d) % 11
print(e)
