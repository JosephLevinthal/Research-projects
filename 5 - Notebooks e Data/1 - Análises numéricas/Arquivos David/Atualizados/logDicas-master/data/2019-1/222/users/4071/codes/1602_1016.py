# primeira lado do triangulo
a = float(input("digite um numero:"))
# segunda lado do triangulo
b = float(input("digite um numero:"))
# terceira lado do triangulo
c = float(input("digite um numero:"))
u = (a+b+c)/2
from math import *
area = sqrt(u*(u-a)*(u-b)*(u-c))
print(round(area, 5))
