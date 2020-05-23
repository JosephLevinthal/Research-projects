from math import*

k = int(input("Insira um numero: "))
x = 0
i = 0

while(i < k):
	x = x + 1/factorial(i)
	i = i + 1
	
print(round(x, 8))