from numpy import*
medias_finais = array(eval(input("Notas finais: ")))
horas_presentes = array(eval(input("Presencas: ")))

carga_horaria = int(input("carga horaria:"))

resul = zeros(3, dtype=int)

frequencia = 75/100 * carga_horaria

for i in range(size(medias_finais)):
	
	if(medias_finais[i] >= 5 and horas_presentes[i] >= frequencia ):
		resul[0] = resul[0] + 1
		
	elif(medias_finais[i] < 5 and 0 <= horas_presentes[i] <= carga_horaria ):
		resul[1] = resul[1] + 1
		
	elif(0 <= medias_finais[i] <= 10 and horas_presentes[i] < frequencia ):
		resul[2] = resul[2] + 1
		
		
print(resul)