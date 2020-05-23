from numpy import*

var = input("cor: ").split(',')
vet = array(var)
a = 0
c = zeros(5, dtype=int)
for i in (vet):
	if vet[i] == "P":
		c[0] = c[0] + 1
	elif vet[i] == "C":
		c[1] = c[1] + 1
	elif vet[i] == "R":
		c[2] = c[2] + 1
	elif vet[i] == "L":
		c[3] = c[3] + 1
	elif vet[i] == "B":
		c[4] = c[4] + 1
	a = a + 1
	print(a)
	