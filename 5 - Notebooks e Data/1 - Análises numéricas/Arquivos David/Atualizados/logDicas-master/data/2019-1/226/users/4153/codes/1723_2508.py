from math import *
n = float(input("Insira o numero real: "))

i = 1
soma = 3

while(n > i):
	soma = soma + ((-1)**(i + 1)) * (4 / ((2*i) * (2*i + 1) * (2 * i +2)))
	i = i + 1 
print(round(soma , 8))