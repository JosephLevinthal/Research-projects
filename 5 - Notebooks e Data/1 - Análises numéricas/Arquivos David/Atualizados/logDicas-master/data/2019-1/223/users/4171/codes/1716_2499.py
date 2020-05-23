from math import factorial

k = int(input("um numero natural k: "))

r = 0 # variavel acumuladora
m = 0 # variavel contadora

while (m < k): # somar r, k vezes
	
	r += (1/factorial(m))
	
	m += 1
	
print(round(r,8))