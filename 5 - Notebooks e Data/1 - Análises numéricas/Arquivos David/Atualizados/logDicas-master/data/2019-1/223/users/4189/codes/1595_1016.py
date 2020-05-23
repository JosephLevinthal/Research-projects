a = float(input("valor de a:"))
b = float(input("valor de b:"))
c = float(input("valor de c "))
s = (a + b + c)/2
from math import sqrt
A = (sqrt(s*(s-a)*(s-b)*(s-c)))
print(round(A,5))