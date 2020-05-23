n = int(input("qtde. de termos: "))
soma = 0
i = 0
from math import*
while (i < n):
	soma = soma + 1 / (factorial(i))
	i = i + 1
neperian = soma
print(round(neperian, 8))