from math import *
n=eval(input("angulos rad: "))
r=int(input("termos: "))
f=1
fa=0
l=1
while(f<=r):
	fa=fa + (((-1)**(f)))*((-n)**(l)/factorial(l))
	f=f+1
	l=l+2
print(round(fa,10))
	