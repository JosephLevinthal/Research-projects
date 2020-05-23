from numpy import *

vet = array(eval(input("alunos por turma: ")))
n = zeros(N, dtype=int)
cont = 0

for x in vet:
	if x/2 != 0:
		cont = cont + 1
		print(cont)
		
for g in vet:
	