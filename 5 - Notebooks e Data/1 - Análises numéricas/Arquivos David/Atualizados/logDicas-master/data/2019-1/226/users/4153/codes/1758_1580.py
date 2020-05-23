from numpy import *
# Vetor de notas
v1 = array(eval(input("Insira um vetor: ")))
# Vetor de nomes
v2 = array(eval(input("Insira um vetor: ")))

i = 0
sf = 0 #soma dos alunos que faltaram
sa = 0 #soma dos alunos aprovados
sr = 0 #soma dos alunos presentes reprovados
while(i < size(v1)):
	if(v1[i] == -1.0):
		sf = sf + 1
	elif(v1[i] >= 6.0):
		sa = sa + 1
	elif((v1[i] != -1.0) and (v1[i] < 6.0)):
		sr = sr + 1
	i = i + 1
x = size(v1) - sf
v3 = zeros(x)
r = 0
h = 0
while(r < size(v1)):
	if(v1[r] != -1):
		v3[h] = v1[r]
		h = h + 1
	r = r +1
q = max(v1)
a = 0
while(v1[a] != max(v1)):
	a = a + 1
	
y = sum(v3)/size(v3)
print(sf)
print(sa)
print(sr)
print(round(y, 2))
print(v2[a])