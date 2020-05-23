a = float(input("qual o lado a?"))
b = float(input("qual o lado b?"))
c = float(input("qual o lado c?"))
s = (a+b+c)/2
from math import*
A = (sqrt(s*(s-a)*(s-b)*(s-c)))
print(round(A, 5))