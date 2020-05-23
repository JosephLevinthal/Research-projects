k = int(input("digite k: "))
from math import *
i = 0
x = 0
while(k>i):
	x= x + 1/factorial(i)
	i= i+1
print(round(x,8))
