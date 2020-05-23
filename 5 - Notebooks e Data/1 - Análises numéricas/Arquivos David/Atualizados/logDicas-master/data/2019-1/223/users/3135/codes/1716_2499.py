from math import *
k = int(input("Insira o valor de k:"))
cont=1
den=1
e=1
while(k > cont):
	e= e + 1 / factorial(den)
	den = den + 1
	cont +=1
print(round(e,8))


