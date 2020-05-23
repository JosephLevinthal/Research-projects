nf= int(input("digite um numero inteiro N maior que zero: "))
i=0
t=nf
s=1
from math import*
while t!=0:
	s=s+((factorial(i)**2)*2**i+1)/factorial(2*i+1)
	t=t-1
	i=i+1
print(round(s,10))