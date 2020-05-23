from math import*
n = int(input("Digite um numero natural: "))
i = 0
total = 0
while(n > 0):
	total = total + sqrt(12) * (1/((2*i + 1) * (3**i))) * ((-1) ** i)
	n = n - 1
	i = i + 1
print(round(total, 8))
	
