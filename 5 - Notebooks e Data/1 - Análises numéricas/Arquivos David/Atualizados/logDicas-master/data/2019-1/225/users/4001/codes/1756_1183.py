from numpy import *
V = array(eval(input("Vetor: ")))

p = 0 #elementos positivos 
i = 0 #contadora

while (i < size(V)):
	if (V[i] > 0):
		p = p + 1
	i = i + 1
i = 0 #posição
z = zeros(p, dtype=int)
p = 0 #contadora
while (p < size(z)):
	if (V[i] >= 0):
	   z[p]=V[i]
	else:
		while(V[i]<0):
			i = i + 1
		z[p]=V[i]
	p = p + 1
	i = i + 1
print(z)
	