from math import*
x=float(input("valor de x:"))

if(x>=-4 and x<0):
	s=x**(1/2)
	f=abs(s)
elif(x==0):
	f=0
elif(x>0 and x<=4):
	f=x**(1/2)
else:
	f="entrada invalida"
print(round(f,4))