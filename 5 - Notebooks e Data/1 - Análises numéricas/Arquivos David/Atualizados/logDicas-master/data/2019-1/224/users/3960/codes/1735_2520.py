from math import *

n = int(input("Insira a quantidade de termos: "))
pi = 0.0
cont = 1

while(cont <= n):
	pi = pi + 1/cont**2
	cont = cont + 1
	
print(round(sqrt(pi*6),6))