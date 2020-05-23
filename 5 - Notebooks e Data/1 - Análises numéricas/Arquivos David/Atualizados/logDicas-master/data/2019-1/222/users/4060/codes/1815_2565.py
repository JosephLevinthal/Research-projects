from numpy import*

media=array(eval(input("informe as medias: ")))
frequencias=array(eval(input("informe as frequencias: ")))
carga_horaria=int(input(" "))
cont=0
v_aux=zeros(3, dtype=int) #vetor com elementos iguais a zero
porcentagem=(75/100)*carga_horaria#75% da carga horaria
for i in media:
	if((i>=5)and(frequencias[cont]>=porcentagem)):#acumula valores para os aprovados
		v_aux[0]=v_aux[0]+1
	elif((i<5)and(frequencias[cont]>=porcentagem)):#acumula valores para reprovados por nota 
		v_aux[1]=v_aux[1]+1
	elif((i>=5)and(frequencias[cont]<porcentagem)):#acumula valores para reprovados por frequencia
		v_aux[2]=v_aux[2]+1
	cont=cont+1

print(v_aux)	
