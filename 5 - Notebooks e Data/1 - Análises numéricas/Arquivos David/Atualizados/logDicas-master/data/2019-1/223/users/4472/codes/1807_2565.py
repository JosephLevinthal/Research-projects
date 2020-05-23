from numpy import *

vetNotas = array(eval(input("Medias dos Alunos: ")))
vetFrequencia = array(eval(input("Frequencia dos Alunos: ")))
cargaHoraria = int(input("Carga horaria da disciplina: "))

vcont = zeros(3, dtype=int)

for i in range(0,len(vetNotas)):
	
	if (vetNotas[i] >= 5) and (vetFrequencia[i] >= 0.75 * cargaHoraria):
		vcont[0] = vcont[0] + 1
		
	elif (vetNotas[i] < 5) and (vetFrequencia[i] >= 0.75 ** cargaHoraria):
		vcont[1] = vcont[1] + 1
		
	else:
		vcont[2] = vcont[2] + 1
		
print(vcont)