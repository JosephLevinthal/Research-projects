from numpy import*
notas = array(eval(input("notas dos alunos: ")))
nomes = array(eval(input("nomes dos alunos: ")))
i = 0
faltaram = 0
aprovados = 0
reprovados = 0
media = 0
l=
while(i<notas[i]):
	if(notas[i] == -1):
		i = i + 1
		faltaram = faltaram + 1
	if(notas[i] >= 6):
		i = i + 1
		aprovados = aprovados + 1
	if(notas[i] < 6):
		i = i + 1
		reprovados = reprovados + 1
	if(notas[i] >= 0):
		i = i + 1
		media = media + sum(notas)/size(notas)
print(faltaram)
print(aprovados)
print(reprovados)
print(round(media, 2))
print(max(nomes[i]))
