from math import *
x = float(input("x: "))
k = int(input("k: "))
soma = 0
i = 1
while (i < k):
	soma = (soma + (x ** i))/(factorial(i))
	i = i + 2
print(round(soma, 9))