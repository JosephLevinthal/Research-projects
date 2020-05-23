a=float(input("lado1: "))
b=float(input("lado2: "))
c=float(input("lado3: "))
from math import*
s=(a+b+c)/2
A=sqrt(s* (s-a)*(s-b)*(s-c))
print(round(A,5))