from math import *

angulo = eval(input("Digite angulo: "))
k = int(input("Digite numero de termos: "))

termogeral=1
seno = 0
sinal = 1
cont = 0
exp=1
while(cont < k):
	seno = seno +(angulo**exp/factorial(termogeral))*sinal
	exp = exp+2
	termogeral = termogeral + 2
	cont = cont + 1
	sinal = sinal*-1
print(round(seno,10))
	
	
	