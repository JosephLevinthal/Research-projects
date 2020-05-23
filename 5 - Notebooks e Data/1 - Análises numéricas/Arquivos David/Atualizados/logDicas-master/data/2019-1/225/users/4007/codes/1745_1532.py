from math import*
x = float(input("digite um numero: "))
k = int(input("qtde. termos: "))
soma = 0
e = 1
d = 1
cont = 0
while (k > cont):
	soma = soma + (x ** e)/factorial(d)
	e = e + 2
	d = d + 2
	cont = cont + 1
print(round(soma, 9))