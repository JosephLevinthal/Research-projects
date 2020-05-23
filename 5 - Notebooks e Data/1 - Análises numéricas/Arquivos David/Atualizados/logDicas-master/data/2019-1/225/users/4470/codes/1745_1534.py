from math import*
x=float(input("numero real:"))
k=int(input("numero inteiro:"))
c=0
d=1
e=0
aux=1
while(c<k):
	e=e+(aux*((x**c)/d))
	if(aux==1):
		aux=-1
	else:
		aux=1
	d=d+2
	c=c+2
print(round(e, 7))