k=int(input("K: "))
a1=0
a2=0
from math import *
while(a1<k):
	a2 = a2 +(1/factorial(a1))
	a1= a1 + 1
print(round(a2,8))
