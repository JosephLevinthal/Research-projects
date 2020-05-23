from numpy import*
#Leitura dos Valores
MF = array(eval(input("Medias finais de cada aluno: ")))
freq = array(eval(input("Frequencia dos alunos: ")))
CH = int(input("Carga Horaria da disciplina: "))
#Resultado final
resultado = zeros(3, dtype = int)
#Numero de aprovados
for i in range(0, size( MF )):
	if (MF[i] >= 5) and (freq[i] >= 0.75 * CH):
		resultado[0] = resultado[0] + 1
#Numero de reprovados por nota
	elif(MF[i] < 5) and (freq[i] >= 0.75 * CH):
		resultado[1] = resultado[1] + 1
#Numero de reprovados por frequencia
	else:
		resultado[2] = resultado[2] + 1
#Impressao dos resultados		
print(resultado)

		
		
		
		
		

		
	