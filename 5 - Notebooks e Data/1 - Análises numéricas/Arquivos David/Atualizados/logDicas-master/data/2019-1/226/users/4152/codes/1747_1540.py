from math import *
x = eval(input("Digite aqui o angulo: "))
k = int(input("Digite aqui o numero de termos da sreie: "))
#Termo Geral = x ** i / factorial(j)
i = 0
j = 0
soma = 0
s = 2
while (i < k):
	soma = soma + ((x ** i) / factorial(j)) * ((-1) ** s)
	i = i + 1
	j = j + 2
	s = s + 1
print(round(soma, 6))