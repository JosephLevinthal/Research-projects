from math import*
xa= float(input("escolha um numero"))
ya= float(input("escolha um numero"))
xb= float(input("escolha um numero"))
yb= float(input("escolha um numero"))
A= (xa,ya)
B= (xb,yb)
d= sqrt((xb-xa)**2 + (yb-ya)**2)
print(round(d, 3))