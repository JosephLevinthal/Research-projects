from math import*
x = eval(input("valor de x: "))
k = int(input("valor de k: "))

soma=0
i=0

while (i<=k-1):
	soma = soma + (-1)**i * (x**(2*i+1))/factorial(2*i+1)
	i = i + 1
print(round(soma, 10))
