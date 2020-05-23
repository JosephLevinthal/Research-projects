from numpy import*
V = array(eval(input("Matriculas: ")))

G2 = 0 #grupo 2

for i in range(size(V)):
	if (V[i] % 2 != 0):
		G2 = G2 + 1
		
G = zeros(G2, dtype=int)
h=0
for i in range(size(V)):
	if (V[i] % 2 != 0):
		G[h] = V[i]
		h+=1
print(G)