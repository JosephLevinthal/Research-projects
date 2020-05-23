from math import *

k = int(input("Insira um numero natural: "))
e = 1.0
cont = 1

while(cont < k):
		e = e + (1.0/factorial(cont))
		cont = cont + 1

print(round(e,8))