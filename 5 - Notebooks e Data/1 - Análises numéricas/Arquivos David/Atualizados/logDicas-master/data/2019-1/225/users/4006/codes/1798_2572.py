from numpy import *
vet = array(eval(input("digite")))
qtd = 0
for i in vet :
	if(i % 2 != 0) :
		qtd += 1
grupo = zeros(qtd, dtype = int)
j = 0
for i in vet :
	if(i % 2 != 0) :
		grupo[j] = i
		j += 1
print(grupo)