a = float(input( ))
b = float(input( ))
c = float(input( ))
from math import sqrt
s= (a+b+c)/2
x = float(s*(s-a)*(s-b)*(s-c))
area= float(sqrt(x))
print(round(area,5))