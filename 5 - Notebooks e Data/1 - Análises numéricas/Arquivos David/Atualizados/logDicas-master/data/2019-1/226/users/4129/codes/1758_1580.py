from numpy import*

notas = array(eval(input("Notas: ")))
alunos = array(eval(input("Alunos :")))
z = 0
rep = 0
apro = 0
y = 0
f = 0      #Faltas
h = 0
k = 0
j = 0
while (h < size(notas)):
	if(notas[h] < 6 and notas[h] >= 0):
		rep = rep + 1
	elif(notas [h] >= 6):
		apro = apro + 1
	elif (notas[h] < 0):
		f = f + 1
	h = h + 1

while(max(notas) != notas[j]):
	k = k + 1
	j = j + 1
	
media = sum(notas) + f
div = size(notas) - f



print(f)
print(apro)
print(rep)
print(round(media/div, 2))
print(alunos[k])



