from numpy import*
from numpy.random import*
n= int(input("Digite o numero de repeticoes: "))

for x in range(n):
	print((n-x)*"*")
	
for x in range(n):
	print((x+1)*"*")