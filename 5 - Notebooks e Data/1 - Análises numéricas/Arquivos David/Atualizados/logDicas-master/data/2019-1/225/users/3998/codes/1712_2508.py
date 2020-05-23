from math import *
k = float(input("numero natural: "))

d = 0      #variavel acumuladora
i = 0         #variavel contadora
e= 0
aux = -1

while (i < k):
	if(i==0):
		e = e+3
	else:
		e = e +(aux *(4/(d *(d+1)*(d+2))))
	
	if (aux==1):
		aux = -1
	else:
		aux = 1
	i = i +1
	d= d+2
print(round(e,8))
		
