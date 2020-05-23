from numpy import*
notas = array(eval(input("Notas: ")))
nomes = array(eval(input("Nomes: ")))
i = 0
faltaram = 0
aprovados = 0
reprovados = 0
media = 0
soma = 0
while(i<size(notas) and i<size(nomes)):
	if(notas[i] == -1):
		faltaram = faltaram + 1
	if(notas[i]>=6 and notas[i]<=10):
		aprovados = aprovados + 1
	if(notas[i]<6 and notas[i]>=0):
		reprovados = reprovados + 1	
	if(notas[i]>=0):
		media = media + notas[i]
		soma = soma + 1
	if(notas[i] == max(notas)):
		n = nomes[i]
	i = i + 1
print(faltaram)
print(aprovados)
print(reprovados)
print(round(sum(media)/soma,2))
print(n)