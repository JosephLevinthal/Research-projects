from math import *
x = int(input("valor das repeticoes: "))

soma = 0
i= 0
fim = x -1

while(i <= fim):
	soma += sqrt(12)*((-1)**i)/( (2*i+1)*3**i)
	i = i + 1

print(round(soma,8))