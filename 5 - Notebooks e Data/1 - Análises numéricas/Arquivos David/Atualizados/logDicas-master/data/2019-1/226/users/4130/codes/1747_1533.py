from math import *

x = float(input("Digite um numero: "))
k = int(input("Quantidade de termos: "))

soma = 1
i = 0
fim = k - 1

while(x < fim):
	soma = soma + (x ** (2 * i)) / (factorial(2 ** i))
	i = i + 1
	print(round(soma, 8))