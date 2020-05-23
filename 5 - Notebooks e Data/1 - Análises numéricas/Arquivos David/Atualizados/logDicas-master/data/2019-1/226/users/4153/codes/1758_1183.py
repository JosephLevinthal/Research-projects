from numpy import *
V = array(eval(input("Insira um vetor nigga: ")))
# Quantidade de elementos negativos:
i = 0
Qp = 0
while(i < size(V)):
	if(V[i] >= 0):
		Qp = Qp + 1
	i = i + 1
# Vetor sem os elementos negativos:
r = 0
s = 0 # contador
v2 = zeros(Qp,dtype=int)
while(r < size(V)):
	if(V[r] >= 0):
		v2[s] = V[r]
		s = s + 1
	r = r + 1
print(v2)