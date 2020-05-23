from math import *
k=int(input())
if(k>0):
	
	i=1
	resultado=0
	while(i<k):
		soma=1/factorial(i)
		resultado=soma+resultado
		i=i+1
	resultado=resultado+1	
	print(round(resultado,8))
