from numpy import*
media=array(eval(input("medias:")))
presenca=array(eval(input("numero de ")))
carga=int(input("carga horaria da disciplina:"))
cont=zeros(3, dtype=int)
for i in range(size(media)):
	if(media[i]>=5 and presenca[i]>=(75/100)*carga):
		cont[0]=1+cont[0]
	elif(media[i]<5 and presenca[i]>(75/100)*carga):
		cont[1]=1+cont[1]
	elif(media[i]>5 and presenca[i]<(75/100)*carga):
		cont[2]=1+cont[2]
print(cont)