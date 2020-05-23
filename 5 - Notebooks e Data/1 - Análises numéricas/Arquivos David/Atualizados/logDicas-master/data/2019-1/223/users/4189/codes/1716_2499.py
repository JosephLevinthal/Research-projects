x = int(input("X:"))
from math import *

n = 0 
e = 0
while(n<x):
	e = e+(1/factorial(n))
	n = n+1
print(round(e,8))