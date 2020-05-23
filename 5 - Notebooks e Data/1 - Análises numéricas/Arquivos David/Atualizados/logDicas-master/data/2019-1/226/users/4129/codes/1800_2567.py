from numpy import*

x = int(input("tamanho: "))
f = zeros(x, dtype=int)
d = "*"

for z in range(size(f)):
	d = "*"
	d = "*"*x
	x = x - 1
	print(d)
for z in range(size(f)+1):
	d = "*"
	d = "*"*x
	x = x + 1
	print(d)