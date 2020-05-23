from numpy import*

n = int(input("tamanho do vetor: "))

x = -2
i = 0
a = -1
v = zeros(n, dtype=int)
while(i < size(v)):
	v[i] = v[x] + v[a]
	v[1] = 1
	i = i + 1
	x = x + 1
	a = a + 1
print (v)