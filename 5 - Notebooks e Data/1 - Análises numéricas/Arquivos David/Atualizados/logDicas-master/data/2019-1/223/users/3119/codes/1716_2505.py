from math import*

angulo = eval(input("Digite o angulo: "))
num = int(input("Digite o numero: ")) - 1
soma = 0 
cont = 0 

while(cont<=num):
	f = ((((-1) ** cont)) * (angulo ** (2 * cont + 1))/(factorial(2 * cont + 1)))
	soma = soma + f
	cont = cont + 1
print(round(soma,10))

