from math import *

n = int(input("Quantidade de termos desejada para a serie: "))

soma = (1/(1*3**0))
pi = sqrt(12)
cont = 1

while(cont < n):
	soma = soma + (-1)**cont * (1/((cont*2+1)*3**cont))
	cont = cont + 1
	
pi = pi * soma
print(round(pi,8))