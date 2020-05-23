a=float(input())
b=float(input())
c=float(input())
s=(a+b+c)/2
from math import*
A=sqrt(s*(s-a)*(s-b)*(s-c))
print(round(A,5))