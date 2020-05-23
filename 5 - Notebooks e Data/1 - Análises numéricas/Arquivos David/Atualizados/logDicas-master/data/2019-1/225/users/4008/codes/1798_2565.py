from numpy import* 
medias = array(eval(input("medias: ")))
presenca = array(eval(input("presenca: ")))
carga = int(input("carga horaria: "))
cont = zeros(3, dtype=int)

for i in range(size(medias)):
	if(medias[i] >=5 and presenca[i] >= (75/100)*carga):
		cont[0] = 1 + cont[0]
	elif(medias[i] <5 and presenca[i] >(75/100)*carga):
		cont[1] = 1 + cont[1]
	elif(medias[i] >= 5 and presenca[i] < (75/100)*carga):
		cont[2] = 1 + cont[2]
print(cont)
	