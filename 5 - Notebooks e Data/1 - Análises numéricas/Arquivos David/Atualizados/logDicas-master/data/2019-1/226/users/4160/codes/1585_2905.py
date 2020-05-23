a = float(input(" Digite o comprimento de um lado do triangulo: "))
b = float(input(" Digite o comprimento de um lado do triangulo: "))
c = float(input(" Digite o comprimento de um lado do triangulo: "))
from math import sqrt
s = (a + b + c )/2
m = sqrt (s*(s - a)*(s - b)*(s - c)) 
print(round(m,5))