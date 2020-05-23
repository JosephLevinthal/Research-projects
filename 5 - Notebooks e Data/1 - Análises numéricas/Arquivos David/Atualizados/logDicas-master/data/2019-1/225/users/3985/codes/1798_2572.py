from numpy import*

V = array(eval(input("Matriculas: ")))
G = 0 #grupo2

for i in range(size(V)):
	if (V[i] % 2 != 0):
		G = G + 1
		
l = zeros(G, dtype=int)
h=0
for i in range(size(V)):
	if (V[i] % 2 != 0):
		l[h] = V[i]
		h+=1
print(l)