from numpy import *
notas = array(eval(input("As notas, nigga: ")))
nomes = array(eval(input("Nomes, nigga: ")))

i = 0
sa = 0 #aprovados
sr = 0 #reprovados
sf = 0 #faltaram
x = 0
maior= -1
while(i < size(notas)):
	if(notas[i]==-1):
		sf = sf + 1
	elif(notas[i]>= 6):
		sa = sa + 1
		x = x + notas[i] 
	elif(notas[i]>= -1 and notas[i] < 6):
		sr = sr + 1
		x = x + notas[i]
	if(notas[i] == max(notas)):
		maior = i
	i = i + 1

print(sf)
print(sa)
print(sr)
m = x / (size(notas) - sf)
print(round(m,2))
print(nomes[maior])
	
	
	