from math import *
k = int(input("Digite um valor k: "))
cont = 1
result = 1
denominador = 1
while (k > cont):
	result = result + (1/factorial(denominador))
	denominador = denominador + 1
	cont = cont + 1
print (round(result,8))