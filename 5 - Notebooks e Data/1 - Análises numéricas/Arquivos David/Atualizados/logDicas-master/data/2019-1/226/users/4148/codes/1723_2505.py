from math import*
a = eval(input("x:"))
k = int(input("series: "))

soma=0
i = 0
fim = k - 1

while(i <= fim):
	soma = soma + (-1) ** i * ((a**(2*i+1)/factorial((2*i+1))))
	i = i + 1

print(round(soma, 10))