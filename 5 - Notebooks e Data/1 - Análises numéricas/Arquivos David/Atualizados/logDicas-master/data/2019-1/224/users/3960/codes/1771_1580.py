from numpy import *

notas = array(eval(input("Insira as notas: ")))
nomes = array(eval(input("Insira os nomes: ")))
cont = 0
f = 0
a = 0
r = 0
n = 1

while(cont < len(notas)):
	if(notas[cont] == -1):
		f += 1
	elif(0 <= notas[cont] < 6):
		r += 1
	elif(6 <= notas[cont] <= 10):
		a += 1
	if(notas[cont] == max(notas)):
		n = cont
	cont += 1
	
print(f)
print(a)
print(r)
print(round(,2))
print(nomes[n])