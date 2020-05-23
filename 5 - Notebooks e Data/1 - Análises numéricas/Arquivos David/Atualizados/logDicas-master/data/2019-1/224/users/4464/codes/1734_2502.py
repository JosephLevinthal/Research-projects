from math import *

n = int(input("insira os n primeiros termos"))

soma = (1/(1*3**0))
raiz = sqrt(12)
cont = 1

while (cont < n):
	soma = soma + (-1)**cont * (1/((cont*2+1)*3**cont))
	cont = cont + 1
										 
raiz = raiz * soma

print(round(raiz,8))