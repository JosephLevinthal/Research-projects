from numpy import *
vetor1 =array(eval(input("digite vetor1: ")))
vetor2 =array(eval(input("digite vetor2: ")))

i = 0
conf = 0
conap = 0
conre = 0
comax = 0

soma = 0
pres = 0
maior = 0
pos = 0

while(i < size(vetor1)):
	if(vetor1[i] == -1):
		conf = conf + 1
	if(vetor1[i] >= 6):
		conap = conap + 1
	if(vetor1[i] > -1 and vetor1[i] < 6):
		conre = 1 + conre
	if(vetor1[i] != -1):
		pres = pres + 1
		soma = soma + vetor1[i]
	if(vetor1[i] > maior):
		maior = vetor1[i]
		pos = i
	i = i + 1

media = soma/pres
print(conf)
print(conap)
print(conre)
print(round(media, 2))
print(vetor2[pos])