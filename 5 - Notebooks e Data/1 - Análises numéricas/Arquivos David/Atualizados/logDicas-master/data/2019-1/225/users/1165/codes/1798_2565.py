from numpy import*
notas=array(eval(input("Notas: ")))# Vetor de nota dos alunos
pre=array(eval(input("Presencas: ")))# Vetor com as presenças na disciplina
car=float(input("Carga horaria: "))# Carga horária da disciplina
v=zeros(3, dtype=int)# Vetor acumulador
lm=car/4#Limite de Faltas
for i in range(size(notas)):
	if(notas[i]>=0 and notas[i]<=10 and car>0 and pre[i]>=0 and pre[i]<=car):# Condições que devem ser atendidas inicialmente
		if (notas[i]>=5 and car-pre[i]<=lm):# Alunos Aprovados
			v[0]=v[0]+1
		if(notas[i]<5):# Reprovados por nota
			v[1]=v[1]+1
		if (car-pre[i]>lm): # Reprovados por frequência
			v[2]=v[2]+1
print(v)