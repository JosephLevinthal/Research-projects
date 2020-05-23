from numpy import *
x = int(input("Numero: "))
d = ""
f = zeros(x, dtype=int)
for i in range(size(f)):
	d = "*"*x
	x = x - 1
	print(d)
for z in range(size(f)+1):
	d = "*"*x
	x = x + 1
	print(d)