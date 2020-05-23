from numpy import *

n = int(input("Insira o numero de * da base: "))
i = n
for l in range(n):
	msg = i * "*"
	print(msg)
	i = i - 1
for r in range(n+1):
	msg2 = r * "*"
	print(msg2)
	r = r + 1