from math import *

x = float(input(":"))
k = int(input(":"))

soma = 0
i = 0

while(i < k):
	soma = soma + (x**i/(factorial(i)))
	i = i + 1
print(round(soma,9))