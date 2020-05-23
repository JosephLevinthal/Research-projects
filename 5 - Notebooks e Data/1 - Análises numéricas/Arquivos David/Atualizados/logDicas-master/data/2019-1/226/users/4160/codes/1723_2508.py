n = int(input("Digite um numero: "))
from math import * 

soma = 3 
i = 1
while (n > i):
	soma = soma + ((-1) ** (i + 1))* (4/ ((2*i) * (2*i + 1) * (2*i + 2)))
	i = i + 1
print(round(soma, 8))