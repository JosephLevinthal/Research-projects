k= int(input("insira um numero natural: "))
from math import*
a=(1/factorial(k))
a=0
s=0
while (s<k):
	a+=(1/factorial(s))
	s+=1
print(round(a,8))