from numpy import *
vet = array(eval(input("Notas finais: ")))
vcont = 0
for i in range(size(vet)): 
	if (vet[i] < 5.0):
		vcont = vcont + 1
print(vcont)