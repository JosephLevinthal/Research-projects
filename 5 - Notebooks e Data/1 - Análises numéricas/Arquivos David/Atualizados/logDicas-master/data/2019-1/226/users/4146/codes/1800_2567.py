from numpy import *
n = int(input("Quantidade: "))
a = "*"
vet = arange(n + 1)

for i in range(n):
	print(n*a)
	n = n - 1
	
for x in vet:
	print(x*a)


	