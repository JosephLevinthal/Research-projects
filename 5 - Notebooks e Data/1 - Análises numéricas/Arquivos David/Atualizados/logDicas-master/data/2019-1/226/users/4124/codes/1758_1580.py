from numpy import *
vn = array(eval(input("Notas dos alunos: ")))
vnomes = array(eval(input("Nomes dos alunos: ")))
fal = 0
apr = 0
rep = 0
soma = 0
i = 0
maior = 0

while(i < size(vn)):
	if(vn[i] == -1):
		fal = fal + 1
	elif(vn[i] >= 6):
		apr = apr + 1
	elif(vn[i] != -1 and vn[i] < 6):
		rep = rep + 1
	if(vn[i] != -1):
		soma = soma + vn[i]
	if(vn[i] == max(vn)):
		maior = i
	i = i + 1

print(fal)
print(apr)
print(rep)
print(round(soma / (size(vn) - fal), 2))
print(vnomes[maior])