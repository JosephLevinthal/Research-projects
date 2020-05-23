from math import *
x = eval(input("Angulo x em radianos:"))
k = int(input("Numero de termos da serie:"))

i = 1
soma = 0
fim = k
cont = 0
n = 2
while(cont<fim):
	soma = soma + ((-1)**n)*(x**i/factorial(i))
	i = i + 2
	cont = cont + 1
	n = n+1
print(round(soma, 10))