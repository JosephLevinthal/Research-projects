from math import*
n=float(input("valor n de termos da serie: "))
pi = sqrt(12)
i= 1
c=0
d=0
soma = 0
if n == 1:
	print(round(pi, 8))
else:
	while c < n:
		sinal= (-1)**c
		soma= soma+ sinal* ((1)/(i*(3**d)))
		c= c+1
		i= i+2
		d= d+1
	print(round(sqrt(12)*soma, 8))
	
