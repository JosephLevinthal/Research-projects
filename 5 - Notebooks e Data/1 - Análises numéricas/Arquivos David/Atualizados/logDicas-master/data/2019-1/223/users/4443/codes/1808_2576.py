from numpy import *
n = int(input("Digite um numero maior que zero: "))
h = 0
i = 0
for i in range(n):
	h = h + 1/(i+1)
print(round(h, 2))	
	