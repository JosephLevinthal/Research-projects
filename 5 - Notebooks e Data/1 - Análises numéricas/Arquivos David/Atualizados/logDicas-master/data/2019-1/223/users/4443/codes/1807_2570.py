from numpy import *
from math import *
r = array(eval(input("Digite um vetor de n reais: ")))
m = mean(r)
n = size(r)
soma = 1
for i in range(n):
	soma = abs(soma * (r[i]-m))
p = soma**(1/n)
print(round(p, 3))	