from math import *
repete=int(input("Quantas vezes o termo se repetira :"))
t=1
e=1
while (repete > 0) and (repete != t) :
	e= e + 1 / factorial(t)
	t=t + 1
print(round(e, 8))