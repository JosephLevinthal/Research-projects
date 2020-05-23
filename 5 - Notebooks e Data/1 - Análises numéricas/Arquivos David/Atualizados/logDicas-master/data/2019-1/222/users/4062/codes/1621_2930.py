from math import*
t = float(input("tempo (seg): "))
g = 9.81
c = 2 * pi
l = ( t/c )  ** 2 
L = g * l
print(L)