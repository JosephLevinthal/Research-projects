from math import *
a = float(input("numero:"))  
b = float(input("numero:"))
c = float(input("numero:"))
s = (a+b+c)/2
Area_triangulo = sqrt(s * (s-a) * (s-b) * (s-c))
print(round(Area_triangulo, 5))
