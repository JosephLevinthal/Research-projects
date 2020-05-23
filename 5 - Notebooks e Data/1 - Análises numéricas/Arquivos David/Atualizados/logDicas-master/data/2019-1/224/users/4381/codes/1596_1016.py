a=float(input("a"))
b=float(input("b"))
c=float(input("c"))
s=a/2+b/2+c/2
from math import *
area=sqrt(s*(s-a)*(s-b)*(s-c))
print(round(area,5))