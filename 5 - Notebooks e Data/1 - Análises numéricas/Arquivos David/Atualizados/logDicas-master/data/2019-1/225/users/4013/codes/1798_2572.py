from numpy import*
vet = array(eval(input("matriculas dos alunos:")))

nimpar = 0
for i in range(size(vet)):
	if(vet[i]%2 != 0):
		nimpar = nimpar + 1
v = zeros(nimpar , dtype=int)
cont = 0
for i in range(size(vet)):
	if(vet[i]%2 != 0):
		v[cont] = vet[i] 
		cont = cont + 1
print(v)