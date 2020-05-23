from math import factorial
k= int(input())
e = 1
indice = 1
if(k == 1):
	print(1.0)
else:
	while( indice < k ):
		e = e + (1 / factorial(indice))
		indice = indice + 1 
print(round(e , 8))
	
	


	