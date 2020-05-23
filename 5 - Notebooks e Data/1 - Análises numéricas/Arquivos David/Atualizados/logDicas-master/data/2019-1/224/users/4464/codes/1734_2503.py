from math import *

n = int(input("Fale a quantidades de termos da serie, macho: "))

soma = 4/1
cont = 1

while (cont < n):
	soma = soma + (-1)**cont * (4/(cont*2+1))
	cont = cont + 1

print(round(soma,8))