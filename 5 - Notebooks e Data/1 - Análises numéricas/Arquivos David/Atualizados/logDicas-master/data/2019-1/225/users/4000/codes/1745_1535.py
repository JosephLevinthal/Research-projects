from math import*
x = float(input("numero real: "))
k = int(input("numero inteiro: "))
e=0
b = 1
c= 0
aux = 1
while(c<k):
	e = e +((aux*(x**b)/b))
	if(aux == 1):
		aux = -1
	else:
		aux = 1
	
	c = c+1
	b = b +2
print(round(e, 6))
		
