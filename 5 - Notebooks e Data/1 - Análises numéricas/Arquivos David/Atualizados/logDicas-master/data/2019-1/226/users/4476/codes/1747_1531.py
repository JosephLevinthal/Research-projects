from math import*
x = eval(input("digite o numero: "))
k = int(input("digite o numero: "))

soma = 0
i = 0
sinal = +1

while (i<=k-1):
	soma = soma + sinal * x**(2*i)/factorial(2*i)
	sinal = - sinal
	i = i + 1
print(round(soma, 10))
