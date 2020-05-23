from numpy import *

vet1 = array(eval(input("Nota: ")))
vet2 = array(eval(input("Nota: ")))

i = 0
cont1 = 0 #variavel contadora de ausentes
cont2 = 0 #variavel contadora de aprovados
cont3 = 0 #variavel contadora de reprovados
cont4 = 0
e = 0
m = max(vet1)

while (i < len(vet1)):
	if vet1[i] == -1 :
		cont1 = cont1 + 1
	if vet1[i] >= 6 :
		cont2 = cont2 + 1
	if vet1[i] < 6 and vet1[i] >= 0 :
		cont3 = cont3 + 1
	if vet1[i] >= 0 :
		cont4 = cont4 + 1
		e = e + vet1[i]
	if m == vet1[i] :
		j = i
	i+=1
print(cont1)
print(cont2)
print(cont3)
print(round(e/cont4, 2))
print(vet2[j])