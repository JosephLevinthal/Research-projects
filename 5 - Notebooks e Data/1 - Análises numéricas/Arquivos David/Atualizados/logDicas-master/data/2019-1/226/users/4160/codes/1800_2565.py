from numpy import * 
vm = array(eval(input("Medias finais: ")))
vp = array(eval(input("Presencas: ")))
vc = int(input("Carga horaria: "))

vet = zeros(3, dtype=int)

for i in range(0,size(vm)):
	if vm[i]>= 5 and vp[i] >= vc*(75/100):
		vet[0] = vet[0] + 1 #aprovado
	elif vm[i]< 5 and vp[i] >= vc*(75/100):
		vet[1] = vet[1] + 1 #reprovado por nota
	elif vm[i]>= 5 and vp[i] < vc*(75/100):
		vet[2] = vet[2] + 1
		
print(vet)
		
