from numpy import*
b = array(eval(input("Digite horas: ")))
m = shape(b)[0]
vet = zeros((m), dtype=int)
for i in range(shape(b)[0]):
	cont=0
	for j in range(7):
		cont = cont+ b[i,j]
		vet[i]= cont
print(vet)

