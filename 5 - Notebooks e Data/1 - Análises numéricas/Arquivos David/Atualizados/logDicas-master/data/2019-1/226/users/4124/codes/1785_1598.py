from numpy import *
vet = array(eval(input("Custo dos itens: ")))
i = 0
soma = 0
desc = 0
while(i < size(vet)):
	soma = soma + vet[i]
	if(vet[i] >= 80):
		desc = desc + 1
	i = i + 1
total = soma - desc * 5
print(round(total,2))
		
	