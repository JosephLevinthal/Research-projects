from math import*
a=float(input(""))
b=float(input(""))
c=radians(float(input("")))

c=sqrt(a**2+b**2-2*a*b*cos(c))

print(round(c,2))