from numpy import *

notas = array(eval(input("Insira as notas: ")))

rep = 0
for i in range(size(notas)):
	if(notas[i] < 5.0):
		rep = rep + 1
print(rep)
ar = zeros(rep, dtype=int)
x = 0
for r in range(size(notas)):
	if(notas[r] < 5):
		ar[x] = r
		x = x + 1
print(ar)