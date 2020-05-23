from numpy import*

media = array(eval(input("media final de cada aluno:")))
horas = array(eval(input("numero de horas dos alunos:")))
ch = array(eval(input("carga horaria:")))

cont = zeros(3, dtype = int)


for i in range (0, size(media)):
	

	if(media[i] >= 5 and (horas[i] >= 0.75 *  ch)):
		cont[0] = cont[0] + 1
		
	elif(media[i] < 5 and (horas[i] >= 0.75 * ch)):
		cont[1] = cont[1] + 1
	
	else:
		cont[2] = cont[2] + 1

print(cont)
		
