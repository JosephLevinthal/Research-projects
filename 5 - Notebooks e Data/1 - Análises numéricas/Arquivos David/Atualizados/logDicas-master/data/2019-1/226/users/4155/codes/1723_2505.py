from math import*
x = eval(input("angulo: "))
k = int(input("termos da serie: "))
soma = 0
i = 0
fim = k - 1
while(i <= fim):
	soma = soma + (-1) ** i * (x **(2 * i + 1))/factorial(2 * i + 1) 
	i = i + 1
print(round(soma, 10))