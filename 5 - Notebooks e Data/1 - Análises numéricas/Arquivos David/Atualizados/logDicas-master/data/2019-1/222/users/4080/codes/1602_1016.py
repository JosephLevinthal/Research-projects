 
A = float(input("valor A: "))
B = float(input("valor B: "))
C = float(input("valor C: "))
S = (A+B+C)/2
from math import *
area = sqrt(S*(S - A)*(S-B)*(S-C))
print(round(area,5))