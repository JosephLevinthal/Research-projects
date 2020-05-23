from math import*
a= float(input("distancia de a:"))
b= float(input("distancia de b:"))
y= float(input("valor do angulo em graus: "))
g= radians(y)
c= sqrt(a**2+b**2-2*a*b*cos(g))
print(round(c, 2))