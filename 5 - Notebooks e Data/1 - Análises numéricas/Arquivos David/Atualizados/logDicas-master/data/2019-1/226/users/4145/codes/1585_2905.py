from math import *
a = float(input("digite o valor do lado a : "))
b = float(input("digite o valor do lado b: "))
c = float(input("digite o valor do lado c: "))
s = (a + b + c)/2
area = ( s * (s - a) * (s - b) * (s - c) )**0.5
print(round(area,5))