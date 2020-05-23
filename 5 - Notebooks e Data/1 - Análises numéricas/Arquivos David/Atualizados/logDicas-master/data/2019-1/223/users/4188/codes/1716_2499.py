n=int(input("entradas: "))
f=0
fa=0
from math import *
while(f<n):
	fa= fa +(1/factorial(f))
	f=f+1
print(round(fa,8))