from math import *

x=eval(input())
k=int(input())
soma=0
t=0

while (t < k):
	ta= (((-1)**t)/factorial(2*t +1))*x**(2*t +1)
	soma = soma + ta
	t = t + 1

print(round(soma, 10))