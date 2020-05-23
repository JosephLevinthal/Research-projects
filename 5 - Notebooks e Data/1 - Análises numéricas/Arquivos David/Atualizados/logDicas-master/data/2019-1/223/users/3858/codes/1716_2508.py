from math import *
k = int(input())
i = 1
a = 2
sinal = 1
soma = 
while(i<k):
	soma = soma + (sinal * ((4)/a*(a+1)*(a+2)))
	a = a +2
	i = i+1
	sinal = sinal*(-1)

print(round(soma,8))