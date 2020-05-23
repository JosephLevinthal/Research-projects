from numpy import *
a = float(input(""))
vo= float(input(""))
N = int(input(""))
t = arange(N)
vet = zeros(N)
cont = 0
while cont < N:
	d = ((a * t ** 2)/ 2) + vo * t
	cont = cont + 1
	vet = d
print(vet)

