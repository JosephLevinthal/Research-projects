from math import sqrt
k= int(input("numero de termos: "))
v1= 0 
v2= 1
i= 0
soma= 0
if(k==1):
	print(sqrt(12))
else:
	while(i<k):
		sinal= (-1)**i
		soma= soma + sinal * (1/(v2*(3**v1)))
		v1= v1 + 1
		v2= v2 + 2
		i= i + 1
	print(round(sqrt(12)*soma, 8))
	