from numpy import *

notas = array(eval(input("Notas: ")))
alunos = array(eval(input("Nomes: ")))

v = 0
i = 0
faltosos = 0
aprovados = 0
reprovados = 0
presentes = 0
k = 0

while i != size(alunos):
	if notas[k] == -1:
		faltosos += 1
	if -1 < notas[k] <= 10:
		v += notas[i]
		presentes += 1
	if 6 <= notas[k] <= 10:
		aprovados += 1
	if 0 <= notas[k] < 6:
		reprovados += 1
	if notas[i] == max(notas):
		maiornota = alunos[i]
	i += 1
	k += 1

c = v / presentes

print(faltosos)
print(aprovados)
print(reprovados)
print(round(c,2))
print(maiornota)