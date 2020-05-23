from numpy import*
N = array(eval(input("Vetor: ")))

v = zeros(size(N), dtype=int)
a = 0 #indice
b = 0
for i in range(size(N)):
	if (N[i] != 0):
		v[a] = N[i]
		a = a + 1
	elif (N[i] == 0):
		v[b] = v[b] + N[i]
		b = b + 1
print(v)
		
		