from numpy import*
media = array(eval(input("digite a media final: ")))
pres = array(eval(input("digite as horas de presenca: ")))
cargah = array(eval(input("digite a carga horaria: ")))

vet = zeros(3, dtype=int)

for i in range(0, size(media)):
	if (media[i]>=5)and(pres[i] >= cargah*(75/100)):
		vet[0] = vet[0] +1 #aprovacao por nota e frequencia ok
	elif media[i]<5:
		vet[1] = vet[1] + 1 #reprovacao por nota
	else:
		vet[2] = vet[2] + 1 #reprovacoes por nota e frequencia ou so por frequencia
print(vet)