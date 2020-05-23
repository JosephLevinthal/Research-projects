from math import*
n = int(input("numero de termos: "))
p = 0
i = 1
while (i <= n):
	p = p + 1 / i ** 2
	i = i + 1

pi = sqrt(p * 6)
print(round(pi, 6))
