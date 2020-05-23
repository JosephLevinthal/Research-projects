from numpy import *

n = int(input("insira o numero:"))

for i in range(n):
	print((n-i) * "*")
	i = i -1 

for i in range(n + 1):
	print(i * "*")
	i = i + 1