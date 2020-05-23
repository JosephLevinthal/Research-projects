from math import*

k = int(input("Valor de k:"))

d = 1
r = 0

while(d <= k - 1):
	s = 1/(factorial(d))
	r = s + r
	d = d + 1
r = r + 1
	
print(round(r, 8))