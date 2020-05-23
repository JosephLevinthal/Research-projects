from math import*
n = int(input("digite qualquer numero: "))
soma = 0
pi1 = (12)**0.5
i = 0

while(n>0):
	soma = soma + (pi1 * (1/((2*i + 1)*(3**i)))*((-1)**i))
	i = i + 1
	n = n - 1
print(round(soma,8))