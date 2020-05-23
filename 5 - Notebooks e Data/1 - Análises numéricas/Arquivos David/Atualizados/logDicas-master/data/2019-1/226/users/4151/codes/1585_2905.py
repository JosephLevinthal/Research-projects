
a=float(input("comprimento de A: "))
b=float(input("comprimento de B: "))
c=float(input("comprimento de C: "))
s=(a+b+c)/2
from math import*
area= sqrt(s*(s-a)*(s-b)*(s-c))
print(round(area,5))



