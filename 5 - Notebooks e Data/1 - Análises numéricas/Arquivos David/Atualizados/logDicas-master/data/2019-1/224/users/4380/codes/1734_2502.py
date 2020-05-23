from math import *
n=int(input("numero de termos: "))
s=0
i=0
f=n-1
while(i<=f):
	s=s+(-1)**(i)*1/((2*i+1)*3**i)*sqrt(12)
	i=i+1
print(round(s,8))