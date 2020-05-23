from math import *
k = int(input("Digite k: "))

soma=0
numero=0

while(numero <k):
	soma = soma + (1/factorial(numero))
	numero = numero +1
	
print(round(soma,8))