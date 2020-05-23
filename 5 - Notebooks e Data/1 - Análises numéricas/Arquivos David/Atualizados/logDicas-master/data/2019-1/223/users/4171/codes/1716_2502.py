from math import *

n = int(input("numero natural: "))

c = 0 #conta
soma = 0 #acumula

while (c < n):
	
	tg = (2*c+1)*(3**c)
	
	soma += (-1)**c / tg
	
	c += 1
	
soma *= sqrt(12)

print(round(soma,8))