a = float (input("Comprimento 1: "))
b = float (input("Comprimento 2: "))
c = float (input("Comprimento 3: "))

s = (a+b+c)/2
from math import*
A = sqrt(s * (s-a) * (s-b) * (s-c))
print (round(A,5))