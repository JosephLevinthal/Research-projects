from numpy import*

notas = array(eval(input("Notas: ")))
nomes = array(eval(input("Nome dos alunos: ")))


i = 0
f = 0
a = 0
r = 0
m = 0
soma = 0

while(i < size(notas) and i < size(nomes)):
	if(notas[i] == -1):
		f = f + 1
	if(notas[i] >= 6 and notas[i] <= 10):
		a = a + 1
	if(notas[i] < 6 and notas[i] >= 0):
		r = r + 1
	if(notas[i] >= 0):
		m = m + notas[i]
		soma = soma + 1
	if(notas[i] == max(notas))	:
		n = nomes[i]
	i = i + 1

print(f)
print(a)
print(r)
print(round(sum(m)/soma, 2))
print(n)

	