from numpy import*
notas = array(eval(input("notas dos alunos:")))
nomes = array(eval(input("nomes dos alunos:")))
d=0 #presentes
i = 0 #posicao nos vetores
j = 0 #faltaram
k = 0 #aprovados
k2= 0
l = 0 #reprovados presentes
l2 = 0
n = 0 #nome da maior nota
while(i < size(notas)):
	if(notas[i] != -1):
		d=d+1
		if(notas[i] >= 6 and notas[i] <=10):
			k = k + 1
			k2 =k2 +notas[i]
		elif(notas[i] < 6 and notas[i] >= 0):
			l = l + 1
			l2 = l2 + notas[i]
	elif(notas[i] == -1):
		j = j + 1
	i = i + 1
i = 0
while(notas[i] != max(notas)):
	i = i + 1
print(j)
print(k)
print(l)
print(round((k2 + l2)/d , 2))
print(nomes[i])
