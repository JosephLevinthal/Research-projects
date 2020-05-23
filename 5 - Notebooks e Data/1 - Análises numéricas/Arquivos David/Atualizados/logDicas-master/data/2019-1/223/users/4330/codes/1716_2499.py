
from math import *

k=int(input("entradas: "))
f=0
F=0

while ( f < k ):
	F = F +(1/factorial(f))
	f += 1
print(round(F,8))
