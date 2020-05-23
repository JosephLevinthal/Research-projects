from math import * 
n = int(input("Numero de vezes:"))

r = sqrt(12)
cont = 0
soma = 0
e = 2 #expoente do menos 1#
expoente = 0 #expoente do quociente#
num = 1 #número da equação que vai variar com mais 2#

while(cont<n):
	
	soma = soma + ((1/(num*(3**expoente)))*((-1) ** e))
	expoente = expoente + 1
	e = e + 1
	cont = cont + 1
	num = num + 2
	pi = sqrt(12) * soma
print(round(pi, 8))
	
	