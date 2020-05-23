from numpy import*

media = array(eval(input("Digite a media final do aluno: ")))
freq = array(eval(input("Digite as horas de frequencia: ")))
carga = int(input("Carga horaria da disciplina: "))

cont = zeros(3, dtype = int)

for i in range(size(media)):
	if((freq[i]/carga) >= 0.75):
		if(media[i] >= 5.0):
			cont[0] = cont[0] + 1
		else:
			cont[1] = cont[1] + 1
	else:
		cont[2] = cont[2] + 1

print(cont)		
	