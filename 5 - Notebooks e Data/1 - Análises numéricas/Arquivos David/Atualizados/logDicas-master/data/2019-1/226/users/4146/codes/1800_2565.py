from numpy import *
notas = array(eval(input("Medias Finais: ")))
horas = array(eval(input("Presenca: ")))
carga = float(input("Carga Horaria: "))
vet = zeros(3, dtype=int)
i = 0

for x in notas:
	if (x >= 5) and (horas[i] >= (carga*0.75)):
		vet[0] = vet[0] + 1
		i = i + 1
	elif (x < 5) and (horas[i] >= (carga*0.75)):
		vet[1] = vet[1] + 1
		i = i + 1
	elif (horas[i] < (carga*0.75)):
		vet[2] = vet[2] + 1
		i = i + 1
		
print(vet)		