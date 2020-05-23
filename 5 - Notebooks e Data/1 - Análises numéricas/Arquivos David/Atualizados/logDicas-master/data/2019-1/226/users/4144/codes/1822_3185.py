from numpy import *
a = input("digite a palavra: ")
aux=""

for i in range(len(a)//2):
	j = len(a) - 1 - i
	aux = a[i]
	a[i] = a[j]
	a[j] = aux
print(aux)