from numpy import *

vt=input("Caracteres: ").upper()

new=vt.replace(' ', '')

cont=0
i=-1
			
while(cont<len(new)):
	if(vt[cont]==vt[i]):
		cont=cont+1
		i=i-1
			
print(new)
print(num)
