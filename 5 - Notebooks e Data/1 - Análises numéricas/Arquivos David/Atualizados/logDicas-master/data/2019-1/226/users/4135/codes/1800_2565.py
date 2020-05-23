from numpy import*
#vetor de medias finais
vetm=array(eval(input("Digite o vetor das medias: ")))
#vetor de presença
vetp=array(eval(input("Digite o vetor de presenca: ")))
#carga horaria da disciplina
c = float(input("Digite a carga horaria: "))
#vetor de contagem
cont= zeros(3, dtype=int)
for i in range(0,size(vetm)):
	if(vetm[i]<5.0):
		cont[1]=cont[1]+1
	elif(vetp[i]/c<0.75):
		cont[2]=cont[2]+1
	else:
		cont[0]=cont[0]+1
		
print(cont)		