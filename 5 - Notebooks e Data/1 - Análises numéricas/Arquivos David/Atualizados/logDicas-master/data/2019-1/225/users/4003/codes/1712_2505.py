from math import*

x = eval(input())
k = int(input())

c = 0
d = 1
sen = 0
aux = 1 # Variável auxiliar pra ficar alternando entre -1 e 1

while(c < k):
	sen  =  sen  + (aux * ((x ** d) / factorial(d)))
	if(aux == 1):
		aux = -1
	else:
		aux = 1
		
	c = c + 1
	d = d + 2
	
print(round(sen, 10))