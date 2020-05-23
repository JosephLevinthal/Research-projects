from math import*
x = eval(input("angulo: "))
k = int(input("serie: "))
cos = 1
if k == 1:
	print(cos)
else:
	for n in range(1, k):
		if n%2 == 0:
			cos = cos + (x**(n*2))/factorial(n*2)
		else:
			cos = cos - (x**(n*2))/factorial(n*2)
	print(round(cos, 11))
