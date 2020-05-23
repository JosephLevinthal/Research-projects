from numpy import *
vn = array(eval(input("Digite o vetor das notas: ")))
na = array(eval(input("Digite o vetor com os nomes dos alunos: ")))
i = 0
j = 0
k = 0
l = 0
while(i < size(vn)):
	if(vn[i] < 0):
		j = j + 1
	elif(vn[i] >= 6):
		k = k + 1
	elif(vn[i] >= 0 and vn[i] < 6):
		l = l + 1
	i = i + 1
m = (sum(vn) + j) / (size(vn) - j)
n = 0
while(vn[n] != max(vn)):
	n = n + 1  
print(j)
print(k)
print(l)
print(round(m, 2))
print(na[n])
