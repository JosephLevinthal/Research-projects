from math import*
a = float(input("A: "))
b = float(input("B: "))
c = float(input("C: "))
s = (a+b+c)/2
at = sqrt(s*(s-a)*(s-b)*(s-c))
print(round(at,5))