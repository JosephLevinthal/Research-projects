from numpy import*

medias = array(eval(input("Medias: ")))
presenca = array(eval(input("Presenca: ")))
carga = int(input())
lista = zeros((3,), dtype=int)
i=0

while(i < size(medias)):
	if (medias[i] > 5 and presenca[i] >= (carga*(75/100))): lista[0]+=1
	elif(medias[i]<5): lista[1]+=1
	else: lista[2]+=1
	i+=1

print(lista)
	
	