from numpy import *
notas = array(eval(input("notas do aluno: ")))
nomes = array(eval(input("nomes dos alunos: ")))
i = 0 #contador
f = 0
a = 0
r = 0
s = 0
sizep = 0
m = 0
while(i<size(notas)):
	if(notas[i] == -1):
		f = f + 1
	if(notas[i] >= 6):
		a = a + 1
	if(notas[i] < 6 and notas[i] != -1):
		r = r + 1
	if(notas[i] != -1):
		s = s + notas[i]
		sizep = sizep + 1
	if(notas[i] == max(notas)):
		m = nomes[i]
	i = i + 1
print(f)
print(a)
print(r)
print(round(s/sizep,2))
print(m)