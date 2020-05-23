from numpy import *

vet = array(eval(input("Alunos de cada turma: ")))

#i = 0
vcont = zeros(size(vet),dtype=int)

for i in range(0,size(vet)):
	
	if vet[i] % 5 == 0:
		vetor2 = vet[1]
		print(size(vetor2))
		print(vet[:])
		
	
	