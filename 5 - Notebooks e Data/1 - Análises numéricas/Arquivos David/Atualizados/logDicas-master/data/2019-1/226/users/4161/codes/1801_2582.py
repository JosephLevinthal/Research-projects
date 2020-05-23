from math import*
x = float(input("angulo: "))
k = int(input("serie: "))
cos = 1
if k == 1:
	print(cos)
else:
	for n in range(1, k):
		cos = cos + (x**(n*2))/factorial(n*2)
	print(round(cos, 8))
