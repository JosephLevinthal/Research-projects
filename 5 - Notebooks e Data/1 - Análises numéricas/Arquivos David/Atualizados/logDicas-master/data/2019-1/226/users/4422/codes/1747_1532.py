from math import *
x = float(input("x: "))
k = int(input("K: "))

soma = 0
i = 0
fim = k

while(i < fim):
	soma = soma + x**(2*i + 1)/factorial(2*i + 1)
	i = i + 1

	
	
print(round(soma , 9))
	