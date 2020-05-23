from numpy import*
from math import*
v= array(eval(input("vetor com n numeros reais positivos: ")))
soma=0
i=0
while (i< size(v)):
	soma= soma + log(v[i] + 1)
	i= i + 1
n= size(v)
divisao= soma/n
M= exp(divisao)- 1
print(round(M, 2))