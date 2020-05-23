from numpy import *
a=input()
aux1=''
aux2=''
if(len(a)%2==0):
	for i in range(len(a)//2):
		j=len(a)-1-i
		aux1=a[i]+aux1
		aux2=aux2 +a[j]

	aux3=aux2+aux1
	print(aux3)
else:
	for i in range(len(a)//2):
		j=len(a)-1-i
		aux1=a[i]+aux1
		aux2=aux2+a[j]
	c=(len(a)//2)
	aux3=aux2+a[c]+aux1
	print(aux3)
	
	
