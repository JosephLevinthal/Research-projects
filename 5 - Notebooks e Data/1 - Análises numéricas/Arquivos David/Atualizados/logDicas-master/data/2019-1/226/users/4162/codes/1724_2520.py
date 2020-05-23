n= int(input("digite um numero N para determinar a quantidade de termos: "))
m=0
d=1
s=0
while m<n:
	s=1/d**2+s
	m=m+1
	d=d+1
from math import*
r=sqrt(6*s)
print(round(r,6))