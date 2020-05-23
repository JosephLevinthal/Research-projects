from math import*
x = float(input("numero real:"))
k = int(input("numero inteiro:"))
soma = 0
m = 0

while(m < k):
	soma = x - (x**2/2) + (x**3/3) - (x**4/4) + (x**5/5)
	m = m + 1
print(round(soma,10))
